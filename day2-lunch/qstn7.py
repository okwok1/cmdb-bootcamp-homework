#!/usr/bin/env python

print "The answer is "

accepted_hits_output = "/Users/cmdb/data/day1/SRR072893_tophatout/accepted_hits.sam"

a = open( accepted_hits_output)

#Count the number of reads that start their alignment on chromosome 2L between base 10000 and 20000 (inclusive)
#Choose lines with chromosome 2L fields[3]

POS = 0
for line in a:
    fields = line.split("\t")
    if line == "":
        break
    elif  10000 <= float(fields[3]) <= 20000 and fields[2] == "2L":
        POS = POS + 1
        
print POS