



words = ['one','two','three','four']
numbers = [1, 2, 3, 4, 5] # zip will drop extra items

ids = zip(words,numbers)
print(ids) # wont work
print(list(ids))



# #wd = 'test'
# wd = {'test': 'test'}
# num = 10

# while num:
# 	#print(wd + str(num))  # no difference
# 	print(f'{wd} - {num}')
# 	num -= 1



# # zip 2 lists in one loop
# words = ['one','two','three','four']
# numbers = [1, 2, 3, 4, 5] # zip will drop extra items

# for index, w in enumerate(words):
# 	num = numbers[index]
# 	print(f'{w} is actualy {num}')

# #for w, n in zip(words, numbers):
# for n, w in zip(numbers, words):  # use ziplongest() to iterate through the longest list
# 	print(f'\n{n} is actualy {w}')

# for value in zip(numbers, words):  # print tuples
# 	print(value)
# 	#print(value[1]) # print second tupple only


# print index with list item
# words = ['one','two','three','four']

# index = 0
# for w in words:
# 	print(index, w)
# 	index += 1

# for index, w in enumerate(words, start = 1): #start of enumeration is 1
# 	print(index, w)


'''
condition = 1

while condition < 10:
	print(condition)
	condition += 1


while True:
	print('infinite loop')
	if True:
		break
	#ctrl+c
'''

# exampleList = [1,2,3,4,5]

# for x in exampleList:
# 	print(x)


# for x in range(2,11):
# 	print(x)





