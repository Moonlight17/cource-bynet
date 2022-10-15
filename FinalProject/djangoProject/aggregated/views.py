# difflib - for comparison emails
import fnmatch
import json
import os
import difflib
import pandas
import pysftp
import paramiko

from datetime import datetime

from aggregated.models import Participants, ListEmails, Aggregate, Lessons
from aggregated.serializers import AggregateSerializer, ParticipantSerializer

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from django.views.decorators.http import require_http_methods, require_GET, require_POST



# VARIABLES
path = ""
data = None
pattern = "participant-*.csv"

# Function for add new participants with emails.

@permission_classes((permissions.AllowAny,))
@require_GET
def add_data_by_default(request):
    fields_names = ['Name', 'status']
    fields_email = ['email', 'Name']
    try:
        df = pandas.read_csv('init_names.csv',
                             encoding="utf-8",
                             header=0,
                             usecols=fields_names)
        for row in df.iterrows():
            Participants.objects.get_or_create(Name=row[1].Name, status=row[1].status)
    except OSError:
        print("ERROR \n Where files with Names data?")
    try:
        df = pandas.read_csv('init_emails.csv',
                             encoding="utf-8",
                             header=0,
                             usecols=fields_email)
        for row in df.iterrows():
            # print(ListEmails.objects.get(user_id__Name=row[1].Name, email=row[1].email))
            ListEmails.objects.get_or_create(user=Participants.objects.get(Name=row[1].Name), email=row[1].email)
    except OSError:
        print("ERROR \n Where files with Email data?")
    parsing_file(request)
    return HttpResponse("Initializing data loaded successfully.")



class MyConnection(pysftp.Connection):
    def __init__(self, *args, **kwargs):
        try:
            if kwargs.get('cnopts') is None:
                kwargs['cnopts'] = pysftp.CnOpts()
        except pysftp.HostKeysException as e:
            self._init_error = True
            raise paramiko.ssh_exception.SSHException(str(e))
        else:
            self._init_error = False

        self._sftp_live = False
        self._transport = None
        super().__init__(*args, **kwargs)

    def __del__(self):
        if not self._init_error:
            self.close()





def similarity(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()


# function for applying inforamtion to DB
def insert_db(data):
    for date in data:
        list_emails = data[date]
        for item in list_emails:
            try:
                email = ListEmails.objects.get(email=item)
                user = Participants.objects.get(pk=email.user.id)
                Aggregate.objects.get_or_create(participant=user, time_on_less=list_emails[item], date=date)
            except ListEmails.DoesNotExist:
                print("Email... ", item, "---", list_emails[item])
                all_mails = ListEmails.objects.all()
                for mail in all_mails:
                    similarity(item, mail.email)
                #     Need send notification in Slack each user
            except Participants.DoesNotExist:
                print("Participants...blya")
                #     Need send notification in Slack Manager the project
    # Write ABOUT PROBLEM!!! (######################---SLACK---######################)


# function for create list with csv's file
def finding_all_csv():
    list_files = []
    file_of_directory = os.listdir(os.path.join(settings.BASE_DIR, 'csv_files'))
    for filename in file_of_directory:
        if fnmatch.fnmatch(filename, pattern):
            list_files.append(filename)
    return list_files

# Function for (create and transorm) or transform date string
def select_date(date_time_str_start, date_time_str_end):
    date_time_str_start = date_time_str_start[2:-1]
    date_time_str_end = date_time_str_end[2:-1]
    date_format='%Y-%m-%d %H:%M:%S'
    date_time_obj_start = datetime.strptime(date_time_str_start, date_format)
    date_time_obj_end = datetime.strptime(date_time_str_end, date_format)
    duration = date_time_obj_end - date_time_obj_start
    duration_in_s = duration.total_seconds()
    dur = divmod(duration_in_s, 60)[0]
    date_time_obj = datetime.strptime(date_time_str_start, date_format)
    if (date_time_obj.weekday() == 1):
        Lessons.objects.get_or_create(meet_date=date_time_obj.date(), status="Of", defaults={'durations': dur-30})
    else:
        Lessons.objects.get_or_create(meet_date=date_time_obj.date(), status="On", defaults={'durations': dur-20})
    return date_time_obj.date()

# Function for reading csv files
def read_csv(file):
    meeting_date = datetime
    result = []
    try:
        df = pandas.read_csv(os.path.join(settings.BASE_DIR, 'csv_files', file),
                             encoding="utf-16",
                             sep="\t",
                             header=0,
                             engine='python')
        meeting_date = select_date(df.loc[0]['Meeting Start Time'], df.loc[0]['Meeting End Time'])
        df[["Attendance Duration"]].replace(r' mins', '')
        df[[str(meeting_date)]] = df[["Attendance Duration"]].replace(regex=[r' mins$'], value='').astype(
            'int64')
        result = df.groupby(by="Attendee Email", dropna=False, sort=False).sum()
        result = json.loads(result.to_json())
    except OSError:
        print("ERROR \n Where files?")
    return result, meeting_date

# Function for downloading csv files from REMOTE_AWS_Machine
def download_files_from_vm():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    path = settings.ENV('REMOTE_FOLDER')
    cinfo = {
        'host': settings.ENV('REMOTE_HOST'),
        'username': settings.ENV('REMOTE_USER'),
        'password': settings.ENV('REMOTE_PASSWORD'),
        'port': int(settings.ENV('REMOTE_PORT')),
        'cnopts': cnopts
    }
    sftp = MyConnection(**cinfo)
    if os.path.exists(os.path.join(settings.BASE_DIR, 'csv_files')):
        pass
    else:
        os.mkdir(os.path.join(settings.BASE_DIR, 'csv_files'))
        print ("CREATED")

    try:
        sftp.get_d(path, os.path.join(settings.BASE_DIR, 'csv_files'), preserve_mtime=True)
    except OSError as e:
        print("osEssor: ", e)
    sftp.close()    

    
@require_http_methods(["GET"])
def parsing_file(request):
    download_files_from_vm()
    list_csv = finding_all_csv()
    data = {}
    all_data = {}
    if len(list_csv):
        for file in list_csv:
            data, date = read_csv(file)
            all_data[list(data.keys())[0]] = data[list(data.keys())[0]]
    else:
        text = 'ERROR \n Where files with attendence?'
        all_data['error'] = text
        return HttpResponse(text)

    insert_db(all_data)
    return HttpResponse("Hello, world. You're at the polls index.")

@require_http_methods(["GET"])
def participants_list(request):
    students = Participants.objects.filter(status='ST').order_by('Name')
    employers = Participants.objects.filter(status='EM').order_by('Name')
    students_ser = ParticipantSerializer(instance=students, many=True)
    employers_ser = ParticipantSerializer(instance=employers, many=True)
    data=[{'label': 'Students', 'options': students_ser.data},{'label': 'Employers', 'options': employers_ser.data}]
    return JsonResponse(data, safe=False)

@require_GET
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def allListBetweenDate(from_date_pr, to_date_pr):
    query = Aggregate.objects.filter(date__range=(from_date_pr, to_date_pr)).order_by('date')
    return query


def allListBetweenDateAndFilters(request, from_date_pr, to_date_pr):
    print('_______________________________')
    # print(request.body)
    data = json.loads(request.body)
    # print(data)

    print('_______________________________')


    try:
        need = data['need']
    except KeyError:
        need = None

    try:
        status = data['status']
    except KeyError:
        status = None


    if need:
        query = Aggregate.objects.filter(date__range=(from_date_pr, to_date_pr), participant_id__in=need).order_by(
            'date')
    elif status != 'All':
        query = Aggregate.objects.filter(date__range=(from_date_pr, to_date_pr), participant__status=status).order_by(
            'date')


    return query

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def my_date_view(request, from_date, to_date):



    result = {}
    from_date_pr = datetime.strptime(from_date, '%d-%m-%Y').date()
    to_date_pr = datetime.strptime(to_date, '%d-%m-%Y').date()




    if request.method == 'GET':
        query = allListBetweenDate(from_date_pr, to_date_pr)
    elif request.method == 'POST':
        query = allListBetweenDateAndFilters(request, from_date_pr, to_date_pr)

    dates = Lessons.objects.filter(meet_date__range=(from_date_pr, to_date_pr)).order_by('meet_date')
    result['dates'] = []
    all_time = 0
    for date in dates:
        all_time = all_time + date.durations
        result['dates'].append({'date': date.meet_date.strftime('%d %B').lstrip("0"), 'status': date.status})
    result['dates'].append(all_time)
    for item in query:

        try:

            result[item.participant.Name]['lessons'][item.date.strftime('%d %B').lstrip("0")]['time'] = item.time_on_less

        except KeyError:
            result[item.participant.Name] = {}
            result[item.participant.Name]['id'] = item.participant.id
            result[item.participant.Name]['name'] = item.participant.Name
            result[item.participant.Name]['status'] = item.participant.status
            result[item.participant.Name]['lessons'] = {}
            for date in dates:
                # print(date)
                result[item.participant.Name]['lessons'][date.meet_date.strftime('%d %B').lstrip("0")] = {'time': 0, 'status': date.status}
            result[item.participant.Name]['lessons'][item.date.strftime('%d %B').lstrip("0")]['time'] = item.time_on_less
    # print(result)
    return JsonResponse(result, safe=False)

