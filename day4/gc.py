#!/usr/bin/env python

import sys

#use own generated .fa file to determine the gc content of the first 500 bp of the transcripts
#print the 

#common_dir = "/Users/cmdb/data/day1/cl-893"
#transcripts_file = "%s/transcripts.gtf" % common_dir
#cufflinks_output = "%s/transcripts.fa" % common_dir
#put in

transcripts = 0

#def revcompl2(x):
#   return ''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])
#print

List = []
while True:
    line = sys.stdin.readline()
    if line == "":
        break
    elif line.startswith( ">" ):
        List.append( "\n" )
        continue
    else:
        List.append( line.strip( "\n" ) )

#print List
Lists = "".join(List)
Lists2 = Lists.split("\n") #this gives a list
#print Lists2[len(Lists2) -1]

nstart=0
nend=500
Lists3 = []
for n in range(1, len(Lists2) ):
    if Lists2[ n ] == "":
        break
    else:
        g = Lists2[ n ].count( 'G', nstart, nend ) #can change this so !start=500 and !end=500
        c = Lists2[ n ].count( 'C', nstart, nend )
        #print g, c
        gc = g + c
        #print gc
        gc_content = gc / float(( nend - nstart ))
        #print gc_content
        Lists3.append( gc_content )
#print sorted(Lists2, key=len)[-100:] #don't need to sort now

orig_stdout = sys.stdout
f = file('gc.dat', 'w')
sys.stdout = f

print Lists3

sys.stdout = orig_stdout
f.close()

orig_stdout = sys.stdout
f = file('gc-flat.dat', 'w')
sys.stdout = f

z = 0
for z in range (1, len(Lists3) ):
    if Lists3[ z ] == "":
        break
    else:
        print Lists3[ z ]

sys.stdout = orig_stdout
f.close()

#this gives a list of 