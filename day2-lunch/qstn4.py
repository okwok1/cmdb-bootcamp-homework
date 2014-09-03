#!/usr/bin/env python

print "The answer is "

accepted_hits_output = "/Users/cmdb/data/day1/SRR072893_tophatout/accepted_hits.sam"

a = open( accepted_hits_output)

#take only the column with the chromosomes

for line in a:
    fields = line.split("\t")
    if line == "":
        break
    else:
        print fields[2]
        
print "End column"