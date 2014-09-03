#!/usr/bin/env python

print "The answer is "

accepted_hits_output = "/Users/cmdb/data/day1/SRR072893_tophatout/accepted_hits.sam"

a = open( accepted_hits_output)

#Calculate the accurate MAPQ Score, which is in column 5
#When developing real programs, want to make as many quality-control steps as possible
#e.g. determining correct file type or if "NH:i" is present

total = 0
for i, line in enumerate(a):
    fields = line.rstrip("\r\n").split("\t")
    if i > 0:
        total = total + float(fields[4])
        
print "Average MAPQ Score: ", total / i