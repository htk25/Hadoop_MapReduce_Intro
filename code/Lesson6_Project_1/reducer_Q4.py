#!/usr/bin/python

import sys

s = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    req = data_mapped
    if "/assets/js/the-associates.js" in req:
        s += 1
print s

