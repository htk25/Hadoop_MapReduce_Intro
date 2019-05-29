#!/usr/bin/python

import sys
ct = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split(" ")
    #print len(data_mapped)
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    thisIP = str(data_mapped[0])
    
    if oldKey and oldKey != thisIP:
        print "{0}\t{1}".format(oldKey, ct)
        ct = 0
    oldKey = thisIP
    ct += 1

if oldKey != None:
    print "{0}\t{1}".format(oldKey, ct)
