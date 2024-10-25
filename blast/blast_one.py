#!/usr/bin/env python3

#working with  problem  sets on blast

import re

dict_one= {}
with open('ss_rand5-200_v_qfo_BL50.txt', 'r') as blast1:
    for line in blast1:
        line = line.rstrip()
        if re.search(r"#",line):   
            continue
        else:
            dict_one =  dict(zip('query id', 'subject id', '% identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score line.split('\t')))
        print(dict_one)

