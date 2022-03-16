import sys

# import importFile
# print(importFile.vTest)



# from importFile import *
# print(vTest)


# sys.path.append('D:\\Space\\Silo\\#3 TECH\\Project\\Code\\Python\\Learning\\import')
# print(sys.path)

# from importFile import *
# print(vTest)


import os

# cwd = os.getcwd()  # current dir
# _path = f'{cwd}\\import'
# print(_path)
# sys.path.append(_path)
# print(sys.path)


# print(os.path.realpath(__file__))  # full path to file
# print(os.path.basename(__file__))  # currect script name

nameFile = os.path.basename(__file__)
#nameScript = nameFile.split('.py')[0]
nameScript = os.path.basename(__file__).split('.py')[0]
print(nameScript)


pathCurrent = os.getcwd()
print(pathCurrent)

path1up = os.path.dirname(pathCurrent)
print(path1up)

path2up = os.path.dirname(path1up)
print(path2up)

