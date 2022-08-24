# all imports
import os, hashlib, sys

# Description all methods

# Function for calculating the Hash
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# Function for creating a list of files without recursion
def only__one_dir(parametr):
    files=[]
    for path in parametr:
        arr = os.listdir(path)
        # norecurse
        for item in arr:
            full_path=os.path.join(path, item)
            if os.path.isfile(full_path):
                files.append(full_path)
    return files

# Function for creating a list of files with recursion
def all_files(parametr):
    files=[]
    for path in parametr:
        for dirpath, dirnames, filenames in os.walk(path):
            # Files
            for filename in filenames:
                # print("File:", os.path.join(dirpath, filename))
                files.append(os.path.join(dirpath, filename))
    return files


# Function for extracting a list of files from arguments
def list_files(parametrs):
    files = []
    for item in parametrs:
            if os.path.isfile(os.path.join(os.curdir, item)) == True:
                files.append(item)
                parametrs.remove(item)
    return files





# Start Program HERE ###!!!###!!!###!!!###!!!###!!!###!!!###!!!###!!!###!!!###
path="."
method=False
# Checking the method of introducing arguments
if (len(sys.argv)>1):
    # print(sys.argv)
    parametrs = sys.argv[1:]
    if "-r" in parametrs:
        print("Recursively")
        method=True
        parametrs.remove("-r")
else:
    # Parametr which set our select Recursive or Not
    recursive = input("Recursively or not? y/N): ").lower()
    if ("y" in recursive)or("+" in recursive):
        print("Recursively")
        method=True
    else:
        print("Not recursively")
        method=False
    print("Now you HERE: ", os.path.dirname(os.path.realpath(__file__)))
    parametrs = input("Enter a list of files and directories: ").split()



files = []
files = list_files(parametrs)

# Which method
if method == True:
    result=all_files(parametrs)
else:
    result=only__one_dir(parametrs)
files=files+result
# print(files)

result={}
for fname in files:
    hash = md5(fname)
    result[fname]=hash
    print(fname, "===>", hash)


# print(result)



python3