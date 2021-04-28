import os

username = ""
userfile = ""
paths = []

def valid_input(prompt, choices):
    while True:
        answer = input(f"{prompt} {choices}").lower()
        if answer in choices:
            return answer
        print('Please choose a valid option.')


def user(userfile):
    userfile = valid_input("Please select your profile name:\n", f"\n{paths}\n")
    print(userfile)


def find_temp():  # Finds the users temp folder. 
    os.chdir("C:\\Users\\")
    start = os.listdir(".")
    for path in start:
        paths.append(path)
    
    user(userfile)
    # os.chdir(f"C:\\Users\\{userfile}\\AppData\\Local\\Temp")




find_temp()
