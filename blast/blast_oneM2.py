#!/usr/bin/env python3

#working wist blast problems set A problem 2,3, finding the longest contig


import sys
file_list = sys.argv[1]
file_list = file_list.split(" ")
hits_files = []
field_str = ['qseqid', 'subid' 'perid','alin','length','mism','gapo', 'qstart', 'qend', 'sstart', 'send', 'eval',' bitsce']

for hit in file_list:
    print(hit)
    with open(hit,'r') as fin:
        for line in fin:
            if line[0] == '#':
                continue

            line = line.rstrip()
            hit_data=dict(zip(field_str, line.split("\t")))
            hit_data['file'] = hit
            hits_files.append(hit_data)
            

print(hits_files)
from tabulate import tabulate
print(tabulate(data, headers="keys"))
