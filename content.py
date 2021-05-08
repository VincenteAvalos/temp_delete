import os, shutil

username = ""
paths = []
deleted = []
remaining = []
folders = []


def find_temp():  # Finds the users temp folder
    os.chdir("C:\\Users\\")
    print(os.listdir())
    start = os.listdir(".")
    for path in start:
        paths.append(path)
        try:
            os.chdir(f"C:\\Users\\{path}\\AppData\\Local\\Temp")
        except PermissionError:
            paths.remove(path)
            print('-----------\n[ErrorNoPerms: '+ path + ']\n==')
        except FileNotFoundError:
            paths.remove(path)
            print('-----------\n[ErrorNotFound: '+ path + ']\n')
    rm_files()
    
def rm_files():  # Removes files in Temp/ directory
    files = os.listdir()
    for file in files:
<<<<<<< HEAD
        try:
            if '.tmp' or '.txt' in file:
                os.remove(file)
                print(file)
            else:
                shutil.rmtree(file)
            deleted.append(file)
        except PermissionError:
            remaining.append(file)
    print(f"{', '.join(remaining)}\n^^^ Could not be deleted...")
    if len(deleted) == 0:
        print("\n>> Nothing was removed...\n")
    else:
        print(f"{deleted}\n * DELETED *\n---")

||||||| b0121ff
        print(file+"\nWILL BE REMOVED\n----------")
=======
        try:
            os.remove(file)
        except PermissionError:
            print(file+ " [PermissionError]")

>>>>>>> e5343aff5bb2781534ddc62a81d9c2d79c03f418

    # print(paths)



find_temp()
# print(os.listdir())
