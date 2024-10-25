#!/usr/bin/env python3

#working with problem set A finding L50 

import re
count = 0
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
#sorted_contig = contigs_list.sort(len(contigs_seq))
sorted_list =  sorted(contig_list,key = lambda sequence : len(sequence))
#print(sorted_list)

l50_contig = [contigs_seq for contigs_seq in sorted_list if len(contigs_seq)>=50]
count+=
print(l50_contig) 

#print(len(l50_contig))
print(l50_contig.count())


#print(len(sorted_list[0]))
#print(len(sorted_list[-1]))
#print(len(sorted_list[33])) #N50 of my contig list

#contig_total_length = "".join(sorted_list)
#print(len(contig_total_length))
#print(sorted_list[34:67])

