#!/usr/bin/env python3
   
#Working with questionsets 7, question 7 method2
import re
seq7 = open("Python_07_ApoI.fasta", "r")
apo_rsites = r"(A|G)AATT(C|T)"
for seq in seq7:
    seq = seq.rstrip()
    if re.search(r"[GA]AATT[CT]",seq):
        seq_cut = re.sub(apo_rsites,r"\1^AATT\2", seq)
        #print(seq_cut)
        cutsites = seq_cut.split("^")
        print(cutsites)

        for fragments in cutsites:
            frag_length = [len(fragments)]
        #sorted_frag = sorted(cutsites)
            print(frag_length)


