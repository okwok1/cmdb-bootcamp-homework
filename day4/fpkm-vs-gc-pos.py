#!/usr/bin/env python

import sys
import pandas
import matplotlib.pyplot as plot
import statsmodels.api as sm

#try to make a linear regression model of fpkm ~ gc

base = "/Users/cmdb/data/day4"

pos = open("FPKM-pos1.txt")
"""
df = pandas.read_table("%s/pos-transcripts-only.gtf" % base )
df2 = pandas.read_table(sys.stdin)
"""
List = []
while True:
    line = pos.readline()
    if line == "":
        break
    else:
        newline = line.replace('"', "")
        List.append( newline.strip( "\n" ) )

oni = open("gc-flat.dat")
#reads in gc-flat.dat

List2 = []
while True:
    line = oni.readline()
    if line == "":
        break
    else:
        List2.append( newline.strip( "\n" ) )

List1 = []
for n in range( 0, len(List)-1 ):
    if List[n] == "":
        break
    else:
        List1[n] = float(List[n])

for n in range( 0, len(List2)-1 ):
    if List2[n] == "":
        break
    else:
        List2x[n] = float(List[n])

#print List2
#d = {}

#for _, sample, sex, stage in df.itertuples(): #takes each row of data frame, returns as tuple
#    d[ sex + "_" + stage ] = pandas.read_table( "%s/%s_clout/genes.fpkm_tracking" % ( base, sample ) )["FPKM"] #gets just the FPKM

#df = pandas.DataFrame( d ) 

#df.to_csv ( "all_fpkms.csv" ) #write data frame to file

"""
par = np.polyfit(xd, yd, 1, full=True)

slope=par[0][0]
intercept=par[0][1]
xl = [min(xd), max(xd)]
yl = [slope*xx + intercept  for xx in xl]
"""
#not sure how to use the above commented code

#df = pandas.read_csv( "all_fpkms.csv", index_col=0)
#unsure how to get lists as readable data for 

model = sm.formula.ols( formula="FPKM ~ GC", data=(List1 ,List2x ) ) #regression formula: left dep, right is indep; names of columns of data

res = model.fit()
print res.summary()

plot.scatter( List1, List2x ) #double-brackets?

plot.savefig( "fpkm-vs-gc.png" )

