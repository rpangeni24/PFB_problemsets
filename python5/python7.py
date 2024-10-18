#!/usr/bin/env python3
#Working with python problem sets 7

#Question 1

import re

count = 0
my_txt = open("Python_07_nobody.txt", "r")
 
for line in my_txt: 
	line = line.rstrip()
	if re.search(r"Nobody",line):
		print("I found")
		count+=1
print(count)
	







