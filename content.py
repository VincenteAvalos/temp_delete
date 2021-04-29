import os

username = ""
paths = []


def find_temp():  # Finds the users temp folder. 
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
            print('-----------\n[ErrorNotFound: '+ path + ']\n==')
    rm_files()
    
def rm_files():
    files = os.listdir()
    for file in files:
        print(file+"\nWILL BE REMOVED\n----------")

    # print(paths)



find_temp()
# print(os.listdir())
