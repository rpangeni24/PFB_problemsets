#!/usr/bin/env python3

import re
count = 0

with open('ecoli_0.25.contigs.fasta', 'r') as contigfile:
    for line in contigfile:
        contigs = line.rstrip()   
        if re.search(r">",contigs):
            count+=1

    print(count)

