#!/usr/bin/env python3 
import sys
number2 =  int(sys.argv[1])
if number2 < 0:
        print('not true')
elif number2 > 20:
        print('number is greater than 20')
elif number2 % 3 == 0:
        print('number is divisible by 3')
else:
        print(number2)

