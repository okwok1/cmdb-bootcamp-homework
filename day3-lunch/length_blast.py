#!/usr/bin/env python

"""
Determine the Blast output by printing the sequence name, ratio of identities, and ratio of gaps
"""

import sys #core utilities; stdin stdout

line = sys.stdin.readline()
assert line.startswith( "BLASTN" ) #this is the file I would expect: a fasta file
sid = line[1:].rstrip("\r\n") #takes all characters after 1st, strips spaces from rear/end of string

#sequences = [] #create list
while True:
    line = sys.stdin.readline()
    if line == "": #stops if the program reaches the end
        break
    if line.startswith( "Query="):
        continue
    if line.startswith( "Query" ):
        fields = line.split("  ")
        number = len(fields[2])
        print fields[2]
    if line.startswith( "Sbjct" ):
        fields = line.split("  ")
        number = len(fields[2])
        print fields[2]
    elif line == "":
        break
    else:
        continue    
        
#catch the ||| character series, then determine the maximum length of this

#sequence = "".join( sequences ) #join together the list using this string as a delimiter; so pushes everything together; not add to string

#print sid, sequence #ID, then sequence