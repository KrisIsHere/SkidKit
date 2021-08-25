import os.path
import requests
import random
from time import sleep

if os.getuid():
    print("Script By KrisIsHere | SkidKit Ver. 1.2.3")
    exit('\nroot access required\n')

version = "1.2.3"

ascii = ["""\x1b[1;33m
   _____ _    _     _ _  ___ _
  / ____| |  (_)   | | |/ (_) |
 | (___ | | ___  __| | ' / _| |_
  \___ \| |/ / |/ _` |  < | | __|
  ____) |   <| | (_| | . \| | |_
 |_____/|_|\_\_|\__,_|_|\_\_|\__|\033[0;37m
""", """\x1b[1;31m
███████ ██   ██ ██ ██████  ██   ██ ██ ████████ 
██      ██  ██  ██ ██   ██ ██  ██  ██    ██    
███████ █████   ██ ██   ██ █████   ██    ██ 
     ██ ██  ██  ██ ██   ██ ██  ██  ██    ██ 
███████ ██   ██ ██ ██████  ██   ██ ██    ██ 
\033[0;37m""", """
\x1b[1;32m.▄▄ · ▄ •▄ ▪  ·▄▄▄▄  ▄ •▄ ▪  ▄▄▄▄▄
▐█ ▀. █▌▄▌▪██ ██▪ ██ █▌▄▌▪██ •██
▄▀▀▀█▄▐▀▀▄·▐█·▐█· ▐█▌▐▀▀▄·▐█· ▐█.▪
▐█▄▪▐█▐█.█▌▐█▌██. ██ ▐█.█▌▐█▌ ▐█▌·
 ▀▀▀▀ ·▀  ▀▀▀▀▀▀▀▀▀• ·▀  ▀▀▀▀ ▀▀▀ \033[0;37m
""", """\033[0;33m
 @@@@@@   @@@  @@@  @@@  @@@@@@@   @@@  @@@  @@@  @@@@@@@
@@@@@@@   @@@  @@@  @@@  @@@@@@@@  @@@  @@@  @@@  @@@@@@@
!@@       @@!  !@@  @@!  @@!  @@@  @@!  !@@  @@!    @@!
!@!       !@!  @!!  !@!  !@!  @!@  !@!  @!!  !@!    !@!
!!@@!!    @!@@!@!   !!@  @!@  !@!  @!@@!@!   !!@    @!!
 !!@!!!   !!@!!!    !!!  !@!  !!!  !!@!!!    !!!    !!!
     !:!  !!: :!!   !!:  !!:  !!!  !!: :!!   !!:    !!:
    !:!   :!:  !:!  :!:  :!:  !:!  :!:  !:!  :!:    :!:
:::: ::    ::  :::   ::   :::: ::   ::  :::   ::     ::
:: : :     :   :::  :    :: :  :    :   :::  :       :
                                                            \033[0;37m
"""]


def setupcheck():
    if os.path.isfile("tools/.info/setup.py"):
        os.system("python3 tools/main.py")
    else:
        os.system("clear")
        print(random.choice(ascii))
        print(os.getcwd())
        setup = input(
            "It appears as tho you have setup your SkidKit would you like to? \033[0;33m(\033[0;33mY\033[92;40m/\033[0;33mN)\33[37m: ")
        if setup == "Y":
            os.system("sudo python3 setup.py")
            os.system("python3 tools/main.py")
        if setup == "y":
            os.system("sudo python3 setup.py")
            os.system("python3 tools/main.py")
        else:
            os.system("clear")
            print(random.choice(ascii))
            sure = input(
                "\033[0;37mAre you sure you dont wanna set it up? \033[0;33m(\033[0;33mY\033[92;40m/\033[0;33mN)\33[37m: ")
            if sure == "Y":
                os.system("python3 tools/main.py")
            if sure == "y":
                os.system("python3 tools/main.py")
            else:
                setupcheck()


def ver_check():
    print('\033[38;2;88;159;240mChecking for Updates.....', end='')
    ver_url = 'https://raw.githubusercontent.com/KrisIsHere/SkidKit/main/tools/version.txt'
    try:
        ver_rqst = requests.get(ver_url)
        ver_sc = ver_rqst.status_code
        if ver_sc == 200:
            github_ver = ver_rqst.text
            github_ver = github_ver.strip()

            if version == github_ver:
                print('\n\033[38;2;88;159;240m[\x1b[1;31mUp-To-Date\033[38;2;88;159;240m]' + '\n')
                setupcheck()
                exit()
            else:
                print('\n\033[38;2;88;159;240m[\x1b[1;31mAvailable\033[38;2;88;159;240m: \x1b[1;31m{}\033[38;2;88;159;240m'.format(github_ver) + ']' + '\n')
                up = input("\033[38;2;88;159;240mWould you like to update? \033[0;33m(\033[0;33mY\033[92;40m/\033[0;33mN)\33[37m: ")
                if up == "y":
                    os.system("rm -rf tools/.info/tools.py")
                    path = os.getcwd()
                    parent = os.path.abspath(os.path.join(path, os.pardir))
                    os.system("cp -r tools/.info " + parent)
                    os.system("cp -r tools/update.py " + parent)
                    os.system("python3 " + parent + "/update.py")
                    sys.exit()
                elif up == "Y":
                    os.system("rm -rf tools/.info/tools.py")
                    path = os.getcwd()
                    parent = os.path.abspath(os.path.join(path, os.pardir))
                    os.system("cp -r tools/.info " + parent)
                    os.system("cp -r tools/update.py " + parent)
                    os.system("python3 " + parent + "/update.py")
                    sys.exit()
                else:
                    exit()

        else:
            print('\033[38;2;88;159;240m[Status\033[38;2;88;159;240m: \x1b[1;31m{} '.format(ver_sc) + '\033[38;2;88;159;240m]' + '\n')
    except Exception as e:
        print('\n \x1b[1;31mException\033[38;2;88;159;240m:\x1b[1;31m ' + str(e))
    exit()


if os.path.isfile("tools/.info/tos_agree.py"):
    ver_check()
else:
    os.system("mkdir tools/.info")
    os.system("clear")
    loooop = "true"
    while loooop == "true":
        print(random.choice(ascii))
        tos_1 = input("""You must agree to our terms and conditions first \033[0;33m(\033[0;33mY\033[92;40m/\033[0;33mN)
    \033[0;37mPress \033[0;33m'\033[0;33mP\033[0;33m'\033[0;37m to view the terms and conditions\33[37m: """)
        if tos_1 == "y":
            loooop = "false"
            os.system("touch tools/.info/tos_agree.py")
            setupcheck()
        if tos_1 == "n":
            sys.exit(1)
        if tos_1 == "p":
            os.system("cat tos.txt")
        if tos_1 == "Y":
            loooop = "false"
            os.system("touch tools/.info/tos_agree.py")
            setupcheck()
        if tos_1 == "N":
            sys.exit(1)
        if tos_1 == "P":
            os.system("cat tos.txt")
