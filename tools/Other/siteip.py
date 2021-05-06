import socket as s
import sys
host = input ("Website: ")
print (f'IP of {host} is {s.gethostbyname(host)}')
sys.exit()

