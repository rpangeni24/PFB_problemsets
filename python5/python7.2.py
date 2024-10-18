#!/usr/bin/env python3

#question 2 of set7

import re

count = 0
my_txt = open("Python_07_nobody.txt", "r")
 
for line in my_txt: 
	line = line.rstrip()
	if re.search(r"Nobody",line):
		new_file = line.replace('Nobody','Rashi')	
		print(new_file)
		

#FIRST TIME SOLVED THIS QUESTION IN THE FIRST GO WITHOTU ANY PROBLEM. :)


