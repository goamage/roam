





# def addEmployee(emp, emp_list=None):  # list will always be empty if not supplied
# 	if emp_list is None:
# 		emp_list = []
# 	emp_list.append(emp)
# 	print(emp_list)

# emps = ['josh', 'jane']

# addEmployee('bob', emps)

# addEmployee('bob')
# addEmployee('bob')
# addEmployee('bob')


# def addEmployee(emp, emp_list=[]):  # if list is not supplied, it is created once at script start
# 	emp_list.append(emp)
# 	print(emp_list)

# emps = ['josh', 'jane']

# addEmployee('bob', emps)

# addEmployee('bob')
# addEmployee('bob')
# addEmployee('bob')



'''

# sys.flags  #check those out in docs

def example(num1,num2):
	answer = num1 - num2
	print('nums are: ', num1, num2)
	print(answer)


example(2,3)
example(num2 = 2, num1 = 3)


def simple(num1, 
		   num2 = 5):
	print (num1, num2)

simple(2)


glob = 'global'

def local():
	glob = 'fail'
	local = 'local'

local()
print(local)
print(glob)


x = 6
def example():
	#global x
	#print(x)
	#print (x+5)
	#x += 6
	globx = x
	print(globx)
	globx += 5
	print (globx)
	
	return globx



example()
print(x)
print('___________')
x = example()
print(x)
'''

# def switchDemo(argument):
# 	switcher = {
# 		1: '3',
# 		2: '2'
# 	}
# 	return switcher.get(argument, 'invalid')

# print(switchDemo(1))
