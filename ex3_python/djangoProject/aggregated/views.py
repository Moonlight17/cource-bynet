from django.shortcuts import render
from django.http import HttpResponse

import os, fnmatch, csv, pandas, difflib, json
from datetime import datetime

# VARIABLES
path=""
data=None
pattern = "participant-*.csv"
column_in_csv=['Meeting Name', 'Meeting Start Time', 'Meeting End Time', 'Name', 'Attendee Email', 'Join Time', 'Leave Time', 'Attendance Duration', 'Connection Type']

# function for create list with csv's file
def finding_all_csv():
    list_files = []
    fileOfDirectory = os.listdir('.')
    for filename in fileOfDirectory:
        if fnmatch.fnmatch(filename, pattern):
            list_files.append(filename)
    return list_files

def select_date(date_time_str):
    date_time_str = date_time_str[2:-1]
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    return date_time_obj.date()

def read_csv(list_csv):
    destiny = pandas.DataFrame()
    for file in list_csv:
        # data = [{}]
        try:
            # print(file)
            df = pandas.read_csv(file,
                                 encoding="utf-16",
                                 sep="\t",
                                 header=0,
                                 engine='python')
            # data = df[['Name']]
            meeting_date = select_date(df.loc[0]['Meeting Start Time'])
            df[['Attendance Duration']].replace(r' mins', '')
            df[['Attendance Duration']] = df[['Attendance Duration']].replace(regex=[r' mins$'], value='').astype('int64')
            result = df.groupby(by='Attendee Email', dropna=False, sort=False).sum()

            print(result['Attendance Duration'])
            # return result.to_json()
            destiny[date] = result['Attendee Email'].map(result)


        except OSError:
            print("kalsdknaoskdn")

        # print(data)
    return destiny, meeting_date



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
