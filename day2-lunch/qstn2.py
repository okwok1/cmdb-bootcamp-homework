#!/usr/bin/env python

print "The answer is "

accepted_hits_output = "/Users/cmdb/data/day1/SRR072893_tophatout/accepted_hits.sam"

a = open( accepted_hits_output)

#match up with NM:i:0 - want to grep this thing

nl = 0
for line in a:
    if "NM:i:0" in line:
        nl = nl + 1

print nl