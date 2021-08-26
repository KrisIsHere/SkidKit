import os
import sys
from sys import platform
path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))
os.chdir(parent)
print(os.getcwd())
print("SkidKit update tool made by KrisIsHere | ver. 1.1")
xd = input("Would you like to update? (Y/N): ")
if xd in ["Y", "y"]:
    os.system("rm -rf SkidKit ; git clone https://github.com/krisishere/SkidKit ; cp -r .info " + parent + "/SkidKit/tools/")
    os.system("rm -rf .info")
    os.chdir(parent + "/SkidKit")
    os.system("python3 main.py")
    sys.exit()
else:
    print("ok")
    sys.exit()
