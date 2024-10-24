#!/usr/bin/env python3

#working with problem set A problem 2,3, finding the longest contig

import re
#count = 0
contig_list= []
with open('ecoli_0.25.contigs.fasta', 'r') as contigfile:
    for line in contigfile:
        contigs_seq = line.rstrip()
        if re.search(r">",contigs_seq):   
            continue
        else:
     
 #print(contigs_seq)    
            

            contig_list.append(contigs_seq)
#print(len(contig_list[0])) 
#sorted_contig = contig_list.sort(len(contigs_seq))
sorted_list =  sorted(contig_list,key = lambda sequence : len(sequence))
#print(sorted_list)
print(len(sorted_list[0]))
print(len(sorted_list[-1]))

print(sorted_list[0])
print(sorted_list[-1])
print(sorted_list[33])
print(sorted_list[34:67])




