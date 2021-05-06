#!/usr/bin/env python3
import sys
import socket
import time
import signal
from timeit import default_timer as timer

host = None
port = 80

maxCount = 10000
count = 0

try:
    host = sys.argv[1]
except IndexError:
    print("Usage: tcpping.py host [port] [maxCount]")
    sys.exit(1)

try:
    port = int(sys.argv[2])
except ValueError:
    print("Error: Port Must be Integer:", sys.argv[3])
    sys.exit(1)
except IndexError:
    pass

try:
    maxCount = int(sys.argv[3])
except ValueError:
    print("Error: Max Count Value Must be Integer", sys.argv[3])
    sys.exit(1)
except IndexError:
    pass

passed = 0
failed = 0


def getResults():
    """ Summarize Results """

    lRate = 0
    if failed != 0:
        lRate = failed / (count) * 100
        lRate = "%.2f" % lRate

    print("\nTCP Ping Results: Connections (Total/Pass/Fail): [{:}/{:}/{:}] (Failed: {:}%)".format((count), passed, failed, str(lRate)))

def signal_handler(signal, frame):
    """ Catch Ctrl-C and Exit """
    getResults()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while count < maxCount:

    count += 1

    success = False

    s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(1)

    s_start = timer()

    try:
        s.connect((host, int(port)))
        s.shutdown(socket.SHUT_RD)
        success = True
    
    except socket.timeout:
        print("Connection timed out!")
        failed += 1
    except OSError as e:
        print("OS Error:", e)
        failed += 1

    s_stop = timer()
    s_runtime = "%.2f" % (1000 * (s_stop - s_start))

    if success:
        print("Connected to %s[%s]: tcp_seq=%s time=%s ms" % (host, port, (count-1), s_runtime))
        passed += 1

    if count < maxCount:
        time.sleep(1)

getResults()

