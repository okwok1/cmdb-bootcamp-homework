#!/usr/bin/env Python

import pandas as pd

cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
df = pd.read_table( cufflinks_output )

dfmedian = df['FPKM'].median()
dfmax = df['FPKM'].max()
dfmin = df['FPKM'].min()
dfrange = dfmax - dfmin

cufflinks_output2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
df2 = pd.read_table( cufflinks_output2 )

df2median = df2['FPKM'].median()
df2max = df2['FPKM'].max()
df2min = df2['FPKM'].min()
df2range = df2max - df2min

import matplotlib.pyplot as plt

#Try to make a box plot for both data sets, each
#Make only one box plot: for FPKMs
#figure out how to make the box plots look like box plots
plt.figure()
plt.yscale('log')

plt.xlabel('male cycle 10')
plt.ylabel('FPKM')
plt.axis([1,5,0.01,100000])
plt.title('male cycle 10')

plt.boxplot(df['FPKM'], 0)

plt.savefig("boxplot1.png")

plt.figure()
plt.yscale('log')

plt.xlabel('female cycle 14')
plt.ylabel('FPKM')
plt.axis([1,5,1,100000])
plt.title('female cycle 14')

plt.boxplot(df2['FPKM'], 0)

plt.savefig("boxplot2.png")

#These box plots look funny.
