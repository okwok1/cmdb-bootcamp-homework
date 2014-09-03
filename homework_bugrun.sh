#!/bin/bash

#
# Day 1 - Homework: Part 2 - debug this bash script
#

echo "There are around 6 mistakes"

FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1
SAMPLE_PREFIX=SRR072 #assigned SRR072 to SAMPLE_PREFIX

GENOME_DIR=/Users/cmdb/data/genomes
GENOME=dmel-all-chromosome-r5.57 #assigned dmel5 to GENOME
ANNOTATION=dmel-all-r5.57.gff

#This is for -p
CORES=4

#added what i is equal to $ONE
for i in {893..916}
do
  echo FastQC $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
  echo TopHat -p$CORES -G $OUTPUT_DIR/gff/$ANNOTATION -o $OUTPUT_DIR/$SAMPLEPREFIX$i\_tophatout --no-novel-juncs --segment-length 20 $GENOME_DIR/$GENOME $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz
  echo CuffLinks -p$CORES -G $OUTPUD_DIR/gff/$ANNOTATION -o $OUTPUT_DIR/cl-$i $OUTPUT_DIR/$SAMPLE_PREFIX$i\_tophatout/accepted_hits.bam
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
#reconfigured TopHat and CuffLinks