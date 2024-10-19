#!/usr/bin/env python3

 #working with problem set7  problem 3 
import re 

fasta_seq  = open("Python_07.fasta", "r")
 
for line in fasta_seq:
	line = line.rstrip()
	header_match = re.search(r"^>\S+",line)
	if header_match:
		print(header_match.group(0))

        

