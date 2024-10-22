#!/usr/bin/env python3
#working with problem set7  problem 4

import re

fasta_seq  = open("Python_07.fasta", "r")
seq_dict = {}
for line in fasta_seq:
	line = line.rstrip()
	if re.search(r"^>(\S+)(\s.+)",line):
		re.search(r"^>(\S+)(\s.+)",line):
		seq_dict[header] = ""
		print('id:',header_match.group(1),'desc:',header_match.group(2))
	else:
	
		seq_dict[header]+=line
		
#seq2 = seq_dict['>gi|603555|emb|X83548.1| H.sapiens gene for histone H4']
#match_seq = re.search(r"(.{10})AA(.{10})CA(.{5})",seq2)
	
#print(match_seq)
#print(seq_dict)

for gene in seq_dict:

	match_seq = re.search(r"(.{10})CATCCAA(.{10})CA(.{5})",seq_dict[gene])
		#print(seq_dict[gene])
		
	print(match_seq)












