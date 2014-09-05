#!/usr/bin/env python

import sys
from translation import Translator

#Find the ORFS in these transcripts, and print all ORFs found
#AUG = start codon; UAA, UAG, UGA = stop codons

common_dir = "/Users/cmdb/data/day1/cl-893"
transcripts_file = "%s/transcripts.gtf" % common_dir
cufflinks_output = "%s/transcripts.fa" % common_dir

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
Lists3 =  sorted(Lists2, key=len)[-100:]

#string = Lists.readline() #this gives an error
#polypeptide = []
#while True:
    #string = Lists.readline()
#    if string == "":
#        break
#    elif "AUG" in string:
#        polypeptide.append( 'start' )
#        if "UUU" in string:
#below is a code taken from a website
bases = ['t', 'c', 'a', 'g']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

def translate(seq):
    seq = seq.lower().replace('\n', '').replace(' ', '')
    peptide = ''
    
    for i in xrange(0, len(seq), 3):
        codon = seq[i: i+3]
        amino_acid = codon_table.get(codon, '*')
        if amino_acid != '*':
            peptide += amino_acid
        else:
            break
                
    return peptide    
#from http://www.petercollingridge.co.uk/book/export/html/474

orig_stdout = sys.stdout
f = file('peptide.fa', 'w')
sys.stdout = f

n = 0
peptide_List = []
for n in range( 1, 100 ):
    string = Lists3[ n ]
    if string == "":
        break
    elif "A" in string:
        print translate( string )
        peptide_List.append(translate( string ))

sys.stdout = orig_stdout
f.close()

#now for the complement
#import string
#complement
#def f(x)
# return x + 1
#f = lambda x: x + 1
#revcompl = lambda x: ' '.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])
#print revcompl("AGTCAGCAT")

#def revcompl2(x):
#   return ' '.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])
#print revcompl("AGTCAGCAT")

#l = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print sorted( l, key=lambda x: x % 2)

#next reading frame
#[0] start1 (go by 3); append after first one
#[1] start2; append second and after second
#[2] start3: append third and after third
#use code from http://kaspermunch.wordpress.com/2013/11/19/finding-open-reading-frames/ or related to find open reading frames

"""

def complement(s): 
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    letters = list(s) 
    letters = [basecomplement[base] for base in letters] 
    return ''.join(letters)
for things in Lists3:
    x = complement(things)
    reverse_complement = x[::-1]
    #print(reverse_complement)

split_reverse_complement = reverse_complement.split('\n')
print spl
orig_stdout = sys.stdout
f = file('peptide2.fa', 'w')
sys.stdout = f

n = 0
peptide_List = []
for n in range( 1, 100 ):
    string = split_reverse_complement[ n ]
    if string == "":
        break
    elif "A" in string:
        print translate( string )
        peptide_List.append(translate( string ))

sys.stdout = orig_stdout
f.close()    

"""
        
#this thing only gives me 100 peptides; cannot figure out how to get all of the peptides from all 6 reading frames
#print sorted(Lists, key=len)[-100:]