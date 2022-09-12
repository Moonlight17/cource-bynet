# difflib - for comparison emails
import fnmatch
import json
import os
import difflib
import pandas

from datetime import datetime

from aggregated.models import Participants, ListEmails, Aggregate, Lessons
from aggregated.serializers import AggregateSerializer, ParticipantSerializer

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# VARIABLES
path = ""
data = None
pattern = "participant-*.csv"


# column_in_csv = ['Meeting Name', 'Meeting Start Time', 'Meeting End Time', 'Name', 'Attendee Email', 'Join Time',
# 'Leave Time', 'Attendance Duration', 'Connection Type']


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
                s = 0
            except Participants.DoesNotExist:
                print("Participants...blya")
                #     Need send notification in Slack Manager the project
    # Write ABOUT PROBLEM!!! (######################---SLACK---######################)


# function for create list with csv's file
def finding_all_csv():
    list_files = []
    fileOfDirectory = os.listdir(os.path.join(settings.BASE_DIR, 'csv_files'))
    for filename in fileOfDirectory:
        if fnmatch.fnmatch(filename, pattern):
            list_files.append(filename)
    return list_files


def select_date(date_time_str):
    date_time_str = date_time_str[2:-1]
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    if (date_time_obj.weekday() == 1):
        Lessons.objects.get_or_create(meet_date=date_time_obj.date(), status="Of")
    else:
        Lessons.objects.get_or_create(meet_date=date_time_obj.date(), status="On")
    return date_time_obj.date()


def read_csv(file):
    meeting_date = datetime
    result = []
    try:
        df = pandas.read_csv(os.path.join(settings.BASE_DIR, 'csv_files', file),
                             encoding="utf-16",
                             sep="\t",
                             header=0,
                             engine='python')
        # data = df[['Name']]
        # print("DFFFFF", df)
        meeting_date = select_date(df.loc[0]['Meeting Start Time'])
        df[["Attendance Duration"]].replace(r' mins', '')
        df[[str(meeting_date)]] = df[["Attendance Duration"]].replace(regex=[r' mins$'], value='').astype(
            'int64')
        result = df.groupby(by="Attendee Email", dropna=False, sort=False).sum()
        result = json.loads(result.to_json())
    except OSError:
        print("ERROR \n Where files?")
    return result, meeting_date


def parsingFile(request):
    list_csv = finding_all_csv()
    data = {}
    all_data = {}
    if len(list_csv):
        for file in list_csv:
            data, date = read_csv(file)
            all_data[list(data.keys())[0]] = data[list(data.keys())[0]]
    else:
        all_data['error'] = "ERROR \n Where files?"
        return HttpResponse("ERROR \n Where files?")

    insert_db(all_data)
    return HttpResponse("Hello, world. You're at the polls index.")


def ParticipantsList(request):
    # query = Participants.objects.all().order_by('Name')
    # serializer = ParticipantSerializer(instance=query, many=True)
    students = Participants.objects.filter(status='ST').order_by('Name')
    employers = Participants.objects.filter(status='EM').order_by('Name')
    students_ser = ParticipantSerializer(instance=students, many=True)
    employers_ser = ParticipantSerializer(instance=employers, many=True)
    data=[{'label': 'Students', 'options': students_ser.data},{'label': 'Employers', 'options': employers_ser.data}]
    return JsonResponse(data, safe=False)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def allListBetweenDate(from_date_pr, to_date_pr):
    query = Aggregate.objects.filter(date__range=(from_date_pr, to_date_pr)).order_by('date')
    return query


def allListBetweenDateAndFilters(request, from_date_pr, to_date_pr):
    data = request.POST
    print("POST:   ", data)
    print(data.getlist('need'))
    try:
        need = data.getlist('need')
    except:
        need = None

    try:
        status = data['status']
    except:
        status = None
    print(need)
    # need = [7, 69, 82]
    if need:
        query = Aggregate.objects.filter(date__range=(from_date_pr, to_date_pr), participant_id__in=need).order_by(
            'date')
    elif status != 'All':
        query = Aggregate.objects.filter(date__range=(from_date_pr, to_date_pr), participant__status=status).order_by(
            'date')

    # query = Aggregate.objects.filter(date__range=(from_date_pr, to_date_pr)).order_by('date')
    return query


@csrf_exempt
def my_date_view(request, from_date, to_date):
    # ===
    # or use strptime to get a date object.
    # from_date_pr = datetime.strptime(from_date, '%Y-%m-%d').date()
    # to_date_pr = datetime.strptime(to_date, '%Y-%m-%d').date()
    # students = Participants.objects.filter(status=0)
    # query = Aggregate.objects.filter(date__range=(from_date_pr, to_date_pr), participant__in=students)
    # serializer = AggregateSerializer(query, many=True)
    # ===

    result = {}
    from_date_pr = datetime.strptime(from_date, '%d-%m-%Y').date()
    to_date_pr = datetime.strptime(to_date, '%d-%m-%Y').date()

    print(from_date_pr)
    print(to_date_pr)

    if request.method == 'GET':
        query = allListBetweenDate(from_date_pr, to_date_pr)
    elif request.method == 'POST':
        query = allListBetweenDateAndFilters(request, from_date_pr, to_date_pr)

    dates = Lessons.objects.filter(meet_date__range=(from_date_pr, to_date_pr)).order_by('meet_date')
    result['dates'] = []
    for date in dates:
        result['dates'].append({'date': date.meet_date.strftime('%d %B').lstrip("0"), 'status': date.status})
    for item in query:
        # print(item)
        try:
            # result[item.participant.Name]['lessons'][item.date.strftime('%d %B').lstrip("0")] = item.time_on_less
            result[item.participant.Name]['lessons'][item.date.strftime('%d %B').lstrip("0")]['time'] = item.time_on_less

        except KeyError:
            result[item.participant.Name] = {}
            result[item.participant.Name]['id'] = item.participant.id
            result[item.participant.Name]['Name'] = item.participant.Name
            result[item.participant.Name]['status'] = item.participant.status
            result[item.participant.Name]['lessons'] = {}
            for date in dates:
                # print(date)
                result[item.participant.Name]['lessons'][date.meet_date.strftime('%d %B').lstrip("0")] = {'time': 0, 'status': date.status}
            result[item.participant.Name]['lessons'][item.date.strftime('%d %B').lstrip("0")]['time'] = item.time_on_less

    return JsonResponse(result, safe=False)

# def getNameandDept(request, salary):
#     users = User.objects.filter(salary__gt=salary)
#
#     return HttpResponse(serializer.serialize(users), mimetype='application/json')
