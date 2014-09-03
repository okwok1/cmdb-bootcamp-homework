#!/bin/bash

#
# Day 1 - Homework: Part 2 - debug this bash script
#

echo "There are around 6 mistakes"

FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1
SAMPLE_PREFIX=SRR072 #assigned SRR072 to SAMPLE_PREFIX

GENOME_DIR=/Users/cmdb/data/genomes
GENOME=dmel-all-chromosome-r5 #assigned dmel5 to X
ANNOTATION=dmel-all-r5.57.gff

CLOUT=_clout

#WHat's this?
CORES=4

#File names
ONE=893
TWO=903
THREE=905
FOUR=915
FIVE=
SIX=
SEVEN=
EIGHT=


#added what i is equal to $ONE
for i in 893
do
  FastQC $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
  TopHat -p1 -G -o $OUTPUT_DIR $GENOME_DIR/$GENOME\.57 $GENOME_DIR/$GENOME\.57.fasta
  CuffLinks -G /Users/cmdb/data/dmel_r5.57_FB2014_03/gff/$ANNOTATION
done
#added the do and done
#removed echo so that the programs can now run
#added -p -G -o --no-novel-junc --segment-length 20 for TopHat
#added -p -G -o for CuffLinks
#FastQC $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR is working properly
#  TopHat -G $GENOME_DIR/$GENOME\.57.fasta $GENOME_DIR/$GENOME\.57.fasta -o $OUTPUT_DIR
#  CuffLinks -G /Users/cmdb/data/results/SRR072893_clout/transcripts\.gtf $OUTPUT_DIR; neither of these are working
#not sure what are the correct inputs for TopHat and CuffLinks; FastQC is the only one working properly
#unsure what genome index base is supposed to mean in: tophat [options]* <genome_index_base> <reads1_1[,...,readsN_1]> [reads1_2,...readsN_2] 
#can't figure out which file to use for CuffLinks