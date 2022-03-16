
class Person():
	pass


person = Person()

person_info = {'first': 'bob', 'last': 'tok'}

for key, value in person_info.items():
	setattr(person, key, value)	

print(person.first)
print(person.last)

for key in person_info.keys():
	print(getattr(person, key))

print(dir(person))
#print(help(person))


# # person.first = 'bob'
# # person.last = 'tok'

# first_key = 'first'
# first_val = 'bob'

# setattr(person, first_key, first_val)



# print(person.first)
# #print(person.last)

# first = getattr(person, first_key)

# print(first)
