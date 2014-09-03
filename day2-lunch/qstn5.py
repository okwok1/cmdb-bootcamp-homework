#!/usr/bin/env python

print "The answer is "

accepted_hits_output = "/Users/cmdb/data/day1/SRR072893_tophatout/accepted_hits.sam"

a = open( accepted_hits_output)

#Count the number of columns with the chromosomes 2L 2R 3L 3R 4 X, separately

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
for line in a:
    fields = line.split("\t")
    if line == "":
        break
    elif fields[2] == "2L":
        n1 = n1 + 1
    elif fields[2] == "2R":
        n2 = n2 + 1
    elif fields[2] == "3L":
        n3 = n3 + 1
    elif fields[2] == "3R":
        n4 = n4 + 1
    elif fields[2] == "4":
        n5 = n5 + 1
    elif fields[2] == "X":
        n6 = n6 + 1

print "# of 2L = ", n1
print "# of 2R = ", n2
print "# of 3L = ", n3
print "# of 3R = ", n4
print "# of 4 = ", n5
print "# of X = ", n6