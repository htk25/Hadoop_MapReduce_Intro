#!/usr/bin/python


import sys


for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, id, username, time, zone, reqMode, req, reqProtocol, status, size = data
        website = "http://www.the-associates.co.uk"
        if(req.find(website) == -1):
            print req
        else:
            print req[req.find(website)+len(website):]
