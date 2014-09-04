#!/usr/bin/env Python

import pandas as pd

#take values from .csv files and compile them.

n = 0
file = (905, 906, 907, 908, 909, 911, 913, 915)
aList = []
for n in file:
    cufflinks_output = "/Users/cmdb/data/day2/samples-%s.csv" % str(n)
    df = pd.read_table( cufflinks_output )
    aList.append(df['FPKM'] ) 

import matplotlib.pyplot as plt

print aList
plt.figure()
plt.plot(aList)
plt.savefig("FPKM_levels.png")
