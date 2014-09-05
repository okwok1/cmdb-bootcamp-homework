#!/usr/bin/env python

import sys

#use the .gtf file as an indexing file
#use the .fa file to find the nucleotide sequences of the transcripts
#print the 

#common_dir = "/Users/cmdb/data/day1/cl-893"
#transcripts_file = "%s/transcripts.gtf" % common_dir
#cufflinks_output = "%s/transcripts.fa" % common_dir
#put in

x = 0
transcripts = 0

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
Lists2 = Lists.split("\n")
print sorted(Lists2, key=len)[-100:]

#unsure whether I would determine the longest assembled transcripts through which file: the .gtf file or the .fa file;
#what was meant by extract?