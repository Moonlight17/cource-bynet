# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# os - find all files
# fnmatch - filter files-csv
# csv - open and work with final csv-file
# pandas - for work with csv-files
# difflib - for comparison emails
import os, fnmatch, csv, pandas, difflib, json

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

def read_csv(list_csv):
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
            df[['Attendance Duration']].replace(r' mins', '')
            df[['Attendance Duration']] = df[['Attendance Duration']].replace(regex=[r' mins$'], value='').astype('int64')
            result = df.groupby(by="Attendee Email", dropna=False, sort=False).sum()

            # print(result)
            # return result.to_json()
            return result


        except OSError:
            print("kalsdknaoskdn")

        # print(data)


# function for adding data to result file
def add_result_file_simple(data):

    try:
        data=data.rename(columns={'Attendance Duration': 'Piska'})
        file = pandas.read_csv('week_grouped.csv')
        result = data.groupby('Attendee Email')

        result=result.sum().reset_index()[['Attendee Email', 'Piska']].to_csv('week_grouped.csv')
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
    # print(similarity('qwertyuio@gmail.com', 'mnbvcxz@gmail.com'))
    # collect_data()
    list_csv = finding_all_csv()
    data = read_csv(list_csv)
    add_result_file_simple(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Должно быть 3 таблицы
# Emails (1-to-many) users
# Пользователи ФИО, почта
# Посещения (День, Юзер, Время)