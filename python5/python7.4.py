#!/usr/bin/env python3
#working with problem set7  problem 4

import re
 
fasta_seq  = open("Python_07.fasta", "r")

for line in fasta_seq:
	line = line.rstrip()
	header_match = re.search(r"^>(\S+)(\s.+)",line)
	if header_match:
		print('id:',header_match.group(1),'desc:',header_match.group(2))
	#else:
		# = re.search(r"^[ATGC]+",line)
		#print(header_match, seq_match)

#for found in re.finditer(r"line1"):
	#seq = found.group (0)
	#line1 = re.search(r"^[ATGC+]

