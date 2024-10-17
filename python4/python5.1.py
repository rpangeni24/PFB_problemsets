#!/usr/bin/env python3
#working with problemsets 5

my_fav = {'book': 'jitterbug perfume', 'song':"Tom petty-I won't back down", 'tree': 'cedar'}
print(my_fav)

#printing a key from the dictionary

print(my_fav['book'])

#pringing out favourite book but using a variable key

fav_thing = 'book'
print(my_fav[fav_thing])

#printing another key from a dictionary

print(my_fav['tree'])

#questioin 5: adding new key to the disctionary

my_fav['organism'] = 'Ecoli'

print(my_fav)
fav_thing = 'organism'
print(my_fav[fav_thing])

my_dict = my_fav

print(my_dict)

#question 6: using a for loop to print out each key and value from the dictionary

for my_dict_key in my_dict:
	print(my_dict_key, my_dict[my_dict_key])


#question 7: getting values from the dictionary


print(my_dict[fav_thing])


