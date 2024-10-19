#!/usr/bin/env python3

#Working with problem sets 8
#Question 1

genes_dict = {}
with open('Python_08.fasta', 'r') as seq_read:
	for line in seq_read:
		line = line.rstrip()
		header,line = line.split("\t")
		count = line.count(nt)
		nt_count[nt] = count
		print('nt count:', nt_count)



