#!/usr/bin/env python

print "The answer is "

accepted_hits_output = "/Users/cmdb/data/day1/SRR072893_tophatout/accepted_hits.sam"

a = open( accepted_hits_output)

nl = 0
while True:
    line = a.readline()
    if line == "":
        break
    nl = nl + 1
print nl
        
    