
str_ = 'test'

print(str_[:-1]) # cut out last char

print(str_.find('t'))  # 1

print('e' in str_)

if 'e' in str_:
	print('true')

print(str_.replace('e', 'a'))
print(str_.replace('e', ''))

str_escape = 'test\'s'
print(str_escape)

str_format = f'{str_} and {str_escape}'
print(str_format.upper())

str_multiline = '''
line 1
line 2
'''

print(type(str_multiline))  #class str
print(str_multiline) 

print('\n' in str_multiline)  # true

print(str_multiline.title())

