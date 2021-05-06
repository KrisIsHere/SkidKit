from scapy.all import *
while True:
      pkt=sniff(filter='tcp', count=1)
      if 'http' or 'https' in pkt.summary():
          print(pkt.summary())
