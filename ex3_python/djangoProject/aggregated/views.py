import fnmatch
import json
import os
import pandas
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse, JsonResponse

# VARIABLES
path = ""
data = None
pattern = "participant-*.csv"
column_in_csv = ['Meeting Name', 'Meeting Start Time', 'Meeting End Time', 'Name', 'Attendee Email', 'Join Time',
                 'Leave Time', 'Attendance Duration', 'Connection Type']


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
        print(type(result.to_json()))
        result=json.loads(result.to_json())
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
    return JsonResponse(all_data)




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
