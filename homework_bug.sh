#!/bin/bash

#
# Day 1 - Homework: Part 2 - debug this bash script
#

echo "There are around 6 mistakes"

FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1
SAMPLE_PREFIX=SRR072 #assigned SRR072 to SAMPLE_PREFIX

GENOME_DIR=/Users/cmdb/data/genomes
GENOME=dmel-all-chomosome-r5.57 #assigned dmel5 to X
ANNOTATION=dmel-all-r5.57.gff

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
for i in $ONE
do
  echo FastQC -o $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz $OUTPUT_DIR
  echo TopHat -p -G -o --no-novel-juncs --segment-length 20 $GENOME_DIR $FASTQ_DIR/$SAMPLE_PREFIX$i\.fasta -o $OUTPUT_DIR
  echo CuffLinks -p -G -o
done
#added the do and done
# removed \ so that . isn't a comment
