#!/usr/bin/env python3

#Working with questionsets 7, question 7
import re
#count = 0
seq7 = open("Python_07_ApoI.fasta", "r")
dict_Rsites = []
for seq in seq7:
	seq = seq.rstrip()
	if re.search(r"[GA]AATT[CT]",seq):
		print('ApoI sites are found')
	

