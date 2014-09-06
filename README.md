cmdb-bootcamp-homework
======================

CMDB Boot Camp Repository
1. 1.36E7
2. 696 (grep --color -c "Sxl" dmel-all-r5.57-removeFASTA.gff)
3. oligonucleotide (cut -f3 dmel-all-r5.57-removeFASTA.gff | uniq)
BAC_cloned_genomic_insert
CDS
DNA_motif
RNAi_reagent
TF_binding_site
TSS
breakpoint
chromosome
chromosome_arm
chromosome_band
complex_substitution
deletion
enhancer
exon
exon_junction
five_prime_UTR
gene
insertion_site
insulator
intron
mRNA
match
match_part
mature_peptide
miRNA
modified_RNA_base_feature
ncRNA
oligonucleotide
origin_of_replication
orthologous_region
orthologous_to
pcr_product
point_mutation
polyA_site
pre_miRNA
protein
protein_binding_site
pseudogene
rRNA
region
regulatory_region
repeat_region
rescue_fragment
sequence_variant
silencer
snRNA
snoRNA
syntenic_region
pcr_product
point_mutation
polyA_site
pre_miRNA
protein
protein_binding_site
pseudogene
rRNA
region
regulatory_region
repeat_region
rescue_fragment
sequence_variant
silencer
snRNA
snoRNA
syntenic_region
tRNA
tandem_repeat
three_prime_UTR
transposable_element
transposable_element_insertion_site
uncharacterized_change_in_nucleotide_sequence

4.  973 BAC_cloned_genomic_insert
108709 CDS
   1 DNA_motif
127571 RNAi_reagent
185819 TF_binding_site
12454 TSS
6653 breakpoint
   1 chromosome
  14 chromosome_arm
5771 chromosome_band
  79 complex_substitution
 818 deletion
 103 enhancer
83955 exon
71382 exon_junction
36888 five_prime_UTR
17294 gene
  48 insertion_site
7683 insulator
71024 intron
30306 mRNA
3658716 match
8067026 match_part
   7 mature_peptide
 304 miRNA
2005 modified_RNA_base_feature
2462 ncRNA
254584 oligonucleotide
8069 origin_of_replication
18819 orthologous_region
613059 orthologous_to
14095 pcr_product
4917 point_mutation
  98 polyA_site
 238 pre_miRNA
30305 protein
1401 protein_binding_site
 239 pseudogene
 161 rRNA
7153 region
2064 regulatory_region
9409 repeat_region
 688 rescue_fragment
 216 sequence_variant
 537 silencer
  31 snRNA
 288 snoRNA
 978 syntenic_region
 314 tRNA
 580 tandem_repeat
27408 three_prime_UTR
5603 transposable_element
65458 transposable_element_insertion_site
  22 uncharacterized_change_in_nucleotide_sequence

==============
Day 4

Task
1. Sample893... 
- Determine GC content of 500 bp region around each transcript
- Build linear regression model of fpkm (log it or something) ~ GC
- Plots with regression line
2. (Advanced) 
- Same thing but with GC content and CpG Content

Hint: can accomplish these with bedtools... involve grep, possibly awk, definitely python

chromosome's gtf file
[] 2L say 1000 -> 2000
transcripts.gtf file
need 750 to 1250

bedtools flank to change the interval
bedtools flank gives 750 - 1000 and 2000-2250 X

use bedtools flank -l 250 (750-1000)
transcripts-250up.gtf (750-1000)

then use ^ as starting file, use -r 250
then (1000-1250) - there are options that retain original piece
transcripts-500.gtf

then use getfasta: which needs gtf file (500) and dmel[...].fasta

getfasta gives back a sequence, not change the interval

but... there is a .fasta.fai file that seemed to have occurred from the getfasta operation. So, used .fasta.fai as <genome>

... files: l-250 *x (1 -> 2 -> 3), then r-500 (3 -> final)
keep the final.gtf files, ran getfasta

pos - take from left side; min - take from right side

FPKM-pos/min.txt files contain FPKM values

Used pos-transcripts-only-final.fa and min-transcripts-only-final.fa (500 bp sections of the genome) for use in determining gc content

ran gc.py to get gc content. have gc.dat and gc-flat.dat
attempted to run fpkm-vs-gc-pos/min.py, but could not get it to perform linear regression or form a line