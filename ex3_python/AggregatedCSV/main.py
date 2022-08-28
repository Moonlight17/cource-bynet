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
        data = [{}]
        try:
            print(file)
            df = pandas.read_csv(file,
                                 encoding="utf-16",
                                 sep="\t",
                                 # index_col='Name',
                                 # parse_dates=['Meeting Start Time', 'Meeting End Time'],
                                 header=0,
                                 # names=column_in_csv,
                                 engine='python')
            # for digit in df['Attendance Duration']:
            #     digit = get_int_minutes(digit)

            # df.groupby(['Name'])
            data = df[['Name']]
            df[['Attendance Duration']].replace(r' mins', '')
            df[['Attendance Duration']] = df[['Attendance Duration']].replace(regex=[r' mins$'], value='').astype('int64')
            # print(df[['Attendance Duration']])
            # result = df.groupby('Name')['Name', 'Attendance Duration'].transform('sum')
            result = df.groupby(by="Attendee Email", dropna=False).sum()

            # print(result)
            # for item in data:
            #     print(data)
            # print(df.update())
            # try:
            #     data[df['Name']] = {
            #         "name": df['Name'],
            #         "time": df['Attendance Duration']
            #
            #     }
            # except OSError:
            #     print("problem with data")

        except OSError:
            print("kalsdknaoskdn")

        # print(data)


# function for adding data to result file
def add_result_file_simple(data):
    # print(type(json.loads(data)))
    try:
        df = pandas.read_csv('result.csv',
                             encoding="utf-16",
                             sep="\t",
                             header=0,
                             engine='python')
        if not df.empty:
            # print(type(data))
            print(data)
            df['TEST1'] = json.loads(data['Attendance Duration'])
            df.to_csv('result.csv',
                      encoding="utf-16",
                      sep="\t",
                      header=True,
                      index=False)
        else:
            print()
        # with open('result.csv') as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     for row in reader:
        #         print(row['first_name'], row['last_name'])
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # collect_data()
    list_csv = finding_all_csv()
    read_csv(list_csv)
    # add_result_file(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
