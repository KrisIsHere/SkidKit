import os
import sys
from sys import platform

if os.getuid():
    print("Script By KrisIsHere | Setup Tool Built 1.0")
    exit('\nroot access required\n')

if platform == "linux" or platform == "linux2":
    path = os.getcwd()
    parent = os.path.abspath(os.path.join(path, os.pardir))
    print(os.getcwd())
    lmao = input("Choose your package manager(1-apt 2-pacman 3-xbps): ")
    if lmao == "1":
            xd = input("Would you like to proceed with the instalation?: (Y/N) ")
            if xd == "y":
                os.system("apt install lolcat putty scapy python3-pip ; pip3 install bane pysocks ; mkdir tools/.info ; touch tools/.info/setup.py")
            elif xd == "Y":
                os.system("apt install lolcat putty scapy python3-pip ; pip3 install bane pysocks ; mkdir tools/.info ; touch tools/.info/setup.py")
            else:
                print("Setup stopped.")
    if lmao == "2":
            xd = input("Would you like to proceed with the instalation?: (Y/N) ")
            if xd == "y":
                os.system("pacman -S lolcat putty scapy python3-pip ; pip3 install bane pysocks ; mkdir tools/.info ; touch tools/.info/setup.py")
            elif xd == "Y":
                os.system("pacman -S lolcat putty scapy python3-pip ; pip3 install bane pysocks ; mkdir tools/.info ; touch tools/.info/setup.py")
            else:
                print("Setup stopped.")
    if lmao == "3":
            xd = input("Would you like to proceed with the instalation?: (Y/N) ")
            if xd == "y":
                os.system("xbps-install -S lolcat putty scapy python3-pip ; pip3 install bane pysocks ; mkdir tools/.info ; touch tools/.info/setup.py")
            elif xd == "Y":
                os.system("xbps-install -S lolcat putty scapy python3-pip ; pip3 install bane pysocks ; mkdir tools/.info ; touch tools/.info/setup.py")
            else:
                print("Setup stopped.")
elif platform == "darwin":
    print("This script is not currently supported for the Mac OS")
elif platform == "win32":
    print("This script is not currently supported for Windows 10 or bellow.")
else:
    print("Platform not recognised...")
    sys.exit()
