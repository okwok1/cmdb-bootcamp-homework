#!/usr/bin/env python

print "The answer is "

accepted_hits_output = "/Users/cmdb/data/day1/SRR072893_tophatout/accepted_hits.sam"

a = open( accepted_hits_output)

#The aim of this program is to count the number of reads that map to exactly one location in the genome
#will use the number of hits; grep on NH:i:1

nl = 0
for line in a:
    if "NH:i:1" in line:
        nl = nl + 1

print nl