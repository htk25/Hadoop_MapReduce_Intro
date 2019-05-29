#!/usr/bin/python


import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, id, username, time, zone, reqMode, req, reqProtocol, status, size = data
        print ip
