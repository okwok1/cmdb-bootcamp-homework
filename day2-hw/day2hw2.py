#!/usr/bin/env Python

import pandas as pd

#Extract Sxl expression for female 1011/12/13/14A/14B/14C/14D

n = 0
file = (905, 906, 907, 908, 909, 911, 913, 915)
for n in file:
    cufflinks_output = "/Users/cmdb/data/results/SRR072%s_clout/genes.fpkm_tracking" % str(n)
    df = pd.read_table( cufflinks_output )
    Sxls = df["gene_short_name"] == "Sxl"
    df[ Sxls ].to_csv("samples-%s.csv" % str(n), sep="\t", index=False)
    
#seem to have problem with indexing: there is a portion with NaN
#removed lines dealing with NaN
#changed it so that there is a == 'Sxl'
#if have access to metadata, use it:
#samples_file = "/Users/cmdb/data/day2/samples.csv"
#samples = pd.read_csv( samples_file)
#cufflinks_dir = "/Users/cmdb/data/results"
#for x in samples[ samples["sex"] == "female"]["sample"]:
#current_df = pd.read_table( cufflinks_dir + x + "_clout/genes.fpkm")