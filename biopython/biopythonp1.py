#!/usr/bin/env python3
#Biopython question 1

from Bio.Seq import Seq

seq1 = Seq('GAATTAAGTTCTTGTGCGCACACAAATCCAATAAAAACTATT')
seq2 = Seq('TTCGCGGTCTCGCTTGTTCTTGTTGTATTCGTATTTT')
protein = seq1.translate()
print(f'[{seq1} translates to {protein}')

import re

fasta_seq  = open("Python_08.fasta", "r")
seq_dict = {}
for line in fasta_seq:
	line = line.rstrip()





