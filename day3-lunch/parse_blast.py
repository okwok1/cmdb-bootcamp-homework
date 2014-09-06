#!/usr/bin/env python

"""
Determine the Blast output by printing the sequence name, ratio of identities, and ratio of gaps
"""

import sys #core utilities; stdin stdout

line = sys.stdin.readline()
assert line.startswith( "BLASTN" ) #this is the file I would expect: a fasta file
sid = line[1:].rstrip("\r\n") #takes all characters after 1st, strips spaces from rear/end of string

#sequences = [] #create list
List = []
while True:
    line = sys.stdin.readline()
    #if line == "": #stops if the program reaches the end
    #    break
    #if line.startswith( "> N" ):
    #    print line.strip("> ")
    #else: #remove the first else so that it doesn't skip the " Identities"
    #    continue
    #if line.startswith( " Identities"):
    #    print line.lstrip()
    #elif line == "":
    #    break
    #else:
    #    continue
    if line == "": #stops if the program reaches the end
        break
    if line.startswith( "Query=" ):
        List.append( line.strip("\n") )
        List.append( "\n")
        print line.strip("\n")
    if line.startswith( "> N" ):
        fields = line.split(" ")
        name = fields[1] #takes the NM/NR name, not the number afterwards
        List.append(name.strip("> "))
        print name.strip("> ")
    if line.startswith( " Identities"):
        one = line.strip(" Identities=") #removes Identities
        two = one.replace(" Gaps =", "") #cuts out Gaps =
        three = two.split(" ")
        List.append(three[0])
        List.append(three[2])
        List.append( "\n" )
        #print two.lstrip()
        print three[0], three[2] #prints out only the ratios, not the percentages
    elif line == "":
        break
    else:
        continue    

Lists = " ".join(List)
print Lists
#sequence = "".join( sequences ) #join together the list using this string as a delimiter; so pushes everything together; not add to string

#print sid, sequence #ID, then sequence; but couldn't figure out the length of the longest consecutively matched sequences