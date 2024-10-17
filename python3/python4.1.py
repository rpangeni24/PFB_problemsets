#!/usr/bin/env python3

import sys          
min = int (sys.argv[1])
max = int(sys.argv[2])+1 
for number in range (min,max):
	if number%2 == 1:
		print(number)

