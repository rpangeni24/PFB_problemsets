#!/usr/bin/env python3
#working with problem set7  problem 4

import re

fasta_seq  = open("Python_07.fasta", "r")
seq_dict = {}
for line in fasta_seq:
	line = line.rstrip()
	if re.search(r"^>(\S+)(\s.+)",line):
		header=line
		seq_dict[header] = ""
		#print('id:',header_match.group(1),'desc:',header_match.group(2))
	else:
	
		seq_dict[header]+=line
		
		match_seq = re.search(r"(.{10})AA(.{10})CA(.{5})",seq_dict[header])
	
print(match_seq)













