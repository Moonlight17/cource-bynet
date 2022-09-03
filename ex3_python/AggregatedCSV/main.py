# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# os - find all files
# fnmatch - filter files-csv
# csv - open and work with final csv-file
# pandas - for work with csv-files
# difflib - for comparison emails
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

#function for transform string mintes to int
def get_int_minutes(text):
    print(text)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def select_date(date_time_str):
    date_time_str = date_time_str[2:-1]
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    return date_time_obj.date()


def read_csv(file):
    destiny = pandas.DataFrame()
    meeting_date = datetime
    try:
        df = pandas.read_csv(file,
                             encoding="utf-16",
                             sep="\t",
                             header=0,
                             engine='python')
        # data = df[['Name']]
        # print("DFFFFF", df)
        meeting_date = select_date(df.loc[0]['Meeting Start Time'])
        df[['Attendance Duration']].replace(r' mins', '')
        df[['Attendance Duration']] = df[['Attendance Duration']].replace(regex=[r' mins$'], value='').astype(
            'int64')
        result = df.groupby(by='Attendee Email', dropna=False, sort=False).sum()

        print("RESULTTTTT:", result.reset_index().to_json(orient='records'))


    except OSError:
        print("kalsdknaoskdn")

        # print(data)
    return destiny, meeting_date


# function for adding data to result file
def add_result_file_simple(data, date):
    try:
        data=data.rename(columns={'Attendance Duration': date})
        file = pandas.read_csv('week_grouped.csv')
        result = data.groupby('Attendee Email')

        result=result.sum().reset_index()[['Attendee Email', date]].to_csv('week_grouped.csv')
        file = pandas.concat([file, result], axis=1)
        # file.append(result, ignore_index=True)

    except FileNotFoundError:
        print("Where file?")
    except pandas.errors.EmptyDataError:
        data = pandas.DataFrame.from_dict(json.loads(data), orient ='index')
        for item in data:
            print(item)
        data.to_csv('result.csv',
                    index=False,
                             encoding="utf-16",
                             sep="\t",
                            # columns=['Email', 'Attendance Duration'],
                             header=1)
        print("###Pizdec###")
    # print(data)

# def collect_data():
#     with open('eggs.csv', newline='') as csvfile:
#         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))



def similarity(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(similarity('estherwah9@gmail.com', 'estherwa@gmai.com'))
    # collect_data()
    # list_csv = finding_all_csv()
    # for file in list_csv:
    #     print("FILE", file)
    #     data, date = read_csv(file)
    #     print("data")
    #     print(data)
    # add_result_file_simple(data, date)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Должно быть 3 таблицы
# Emails (1-to-many) users
# Пользователи ФИО, почта
# Посещения (День, Юзер, Время)