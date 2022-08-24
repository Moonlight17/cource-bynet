import os, sys

path="."
method=False



def non_recurse(path):
    arr = os.listdir(path)
    # norecurse
    for item in arr:
        if os.path.isfile(os.path.join(path, item)):
            print("File: ",item)
        else:
            print("Folder: ",item)

def recurse(path):
    for dirpath, dirnames, filenames in os.walk(path):
        # Folders
        for dirname in dirnames:
            print("Folder:", os.path.join(dirpath, dirname))
        # Files
        for filename in filenames:
            print("File:", os.path.join(dirpath, filename))



if (len(sys.argv)>1):
    # print(sys.argv)
    parametrs = sys.argv[1:]
    if "-r" in parametrs:
        print("Recursively")
        method=True
        parametrs.remove("-r")
else:
    # Parametr which set our select Recursive or Not
    recursive = input("Recursively or not? y/N): ")
    if ("y" in recursive)or("Y" in recursive)or("+" in recursive):
        print("Recursively")
        method=True
    else:
        print("Not recursively")
        method=False
    parametrs = input("Enter a directory: ")



print(parametrs)
# Which method
if method == True:
    recurse(parametrs[0])
else:
    non_recurse(parametrs[0])




