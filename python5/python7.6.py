#!/usr/bin/env python3
#working with problemsets7 problem6 


#working with problemsets7 problem6 

import re
count = 0
seq7 = open("Python_07_ApoI.fasta", "r")
for line in seq7:
	seq = line.rstrip()
	if re.search(r"[GA]AATT[CT]",seq):
		print ("ApoI site found")
	else:
		print("No ApoI site in this line")	

#for just additional work, if I want to cont the number of cuts, I add count=0 in the top and tthen do the additional command below

		count+=1
print("total apoI site:", count)

