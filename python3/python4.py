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






