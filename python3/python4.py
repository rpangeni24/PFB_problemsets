#!/usr/bin/env python3
#This file is for python problems set 4 on day3. 
my_fav = ['reading', 'writing', 'coding', 'musics', 'walking']
print(my_fav)

#getting middle element in the list
my_fav[2]
#creating a different variable for middle element
middle_ele = my_fav[2]
print(middle_ele)

#replacing middle element with a new element

my_fav[2] = 'pythoning'
print(my_fav)

my_fav.append('running')
print(my_fav)
my_fav.insert(0,'sleeping')
print(my_fav)
my_fav.pop()
print(my_fav)
my_fav.pop(0)
print(my_fav)
my_fav.pop(2)
print(my_fav)

#question sets2 starting from here
taxa_string = 'sapiens : erectus : neanderthalensis'
print(taxa_string)

#This is just another method to treat each word as separate element in addition. 
taxa_string1 = 'sapiens'':''erectus'':''neanderthalensis'
print (taxa_string)

taxa_string.split(':')
taxa_list = taxa_string.split(':')
print(taxa_list)

print(sorted (taxa_list))
sorted_list = sorted(taxa_list)
print(sorted_list)

print(taxa_list)
taxa_list.sort()
print(taxa_list)
#question 3 creating a new variable called my_list

my_list = ['a','bb', 'ccc']
list_copy = my_list
print(my_list)

#question 4 printing out numbers 1 to 100 using while loop

count = 1
while count < 101:
	print("count:", count)
	count+=1
print("done")

#finding factorial of 1000

n = 3
f = 1
while n>0:
  print("n ", n)
  f*=n
  n-=1
  print (f)
print("f ",f)
print("done")


# workiing with question 6

numbers = [101,2,15,22,95,33,2,27,72,15,52]
for number in numbers:
	if number%2 == 0:
		print(number)


#Question 7

numbers.sort()
print(numbers)

print(numbers)

for number in numbers:
	print(number)
sum_even = 0
sum_odd = 0
for number in numbers:
	if number%2 == 0:
  		sum_even+=number
	else: 
		sum_odd+=number
print(sum_even, sum_odd)

print('sum of even numbers:',sum_even, 'sum of odds:',sum_odd)

#Question 8 for loop using range function

range(100)
range(0,100)
for num in range(100) :
	print(num)

#questioin 9: Modified script for numbers 1 to 100

range(101)
range(1,101)
for num in range(101) :
	print(num)
#Question 10
import sys 

min =int( sys.argv[1])
max = int(sys.argv[2])+1
for num in range(min, max):
	print(num)

#Question 11

import sys
 
min = int (sys.argv[1]) 
max = int(sys.argv[2])+1

for number in range (min,max):
	if number%2 == 1:
		print(number)



#Question 13 

dnaseqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for dnaseq in dnaseqs:
	print(dnaseq)











