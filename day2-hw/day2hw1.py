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

#print df.describe(percentiles=[0.33, 0.66])["FPKM"]
#print df2.describe(percentiles=[0.33, 0.66])["FPKM"]

#df_33ile = 0
#df_66ile = 16.637064
#df2_33ile = 0.059101
#df2_66ile = 10.313248

#male_bottom = df[ df["FPKM"] < df_33ile]
#male_middle = df[ df[df["FPKM"] < df_66ile ] >= df_33ile]
#male_top = df[ df["FPKM"] >= df_66ile]
#female_bottom = df2[ df2["FPKM"] < df2_33ile]
#female_middle = df2[ df2[df2["FPKM"] < df2_66ile] >= df2_33ile]
#female_top = df2[ df2["FPKM"] >= df2_66ile]
sortM = df.sort("FPKM", ascending=True)
sortF = df2.sort("FPKM", ascending=True)

bottom_male = sortM[0:5196]["FPKM"]
middle_male = sortM[5196:10390]["FPKM"]
top_male = sortM[10390:15603]["FPKM"]
bottom_female = sortF[0:5196]["FPKM"]
middle_female = sortF[5196:10390]["FPKM"]
top_female = sortF[10390:15603]["FPKM"]

boxplot_data = [bottom_male, middle_male, top_male, bottom_female, middle_female, top_female]

import matplotlib.pyplot as plt

#Try to make a box plot for both data sets, each
#Make only one box plot: for FPKMs
#figure out how to make the box plots look like box plots
plt.figure()

#plt.ylabel('FPKM')
#plt.axis([0,7,0,220])
plt.ylim(-10,100)
#plt.title('')
plt.boxplot( boxplot_data )
plt.savefig("boxplot1.png")

#These box plots look funny.
