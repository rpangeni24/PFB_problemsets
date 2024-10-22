#!/usr/bin/env python3
#working with problemsets7 problem6 


#working with problemsets7 problem6 

import re
 
seq7 = open("Python_07_ApoI.fasta", "r")

seq_dict = {'seq1':}
for line in seq7:
    seq = line.rstrip()
    if line.startswith('>'):
        line.append(line[1:-1])
    else:
        seq.append(line)
    if re.search(r"[GA]AATT[CT]",seq):
    
        print(seq)


        
   


#for just additional work, if I want to cont the number of cuts, I add count=0 in the top and tthen do the additional command below

#print("total apoI site:", count)


