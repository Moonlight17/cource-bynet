# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# os - find all files
# fnmatch - filter files-csv
# re - parse date from name's file
# pandas - for work with csv-files
import os, fnmatch, re, pandas

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
            data['AttNoMin'] = df[['Attendance Duration']].apply(lambda time: time.str.split().str[0].astype('int64'))
            result = data.groupby('Name')['AttNoMin'].sum()
            # count = data.shape[0]
            print(result)
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
def add_result_file():
    # Use a breakpoint in the code line below to debug your script.
    try:
        main_file = csv.read_csv("C:/Users/kennethcassel/homes.csv")
    except:
        print("not work!!!")
        ef = open('./main.csv', 'x')
        ef.close()

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
