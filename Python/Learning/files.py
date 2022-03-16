
f = open('test.txt','r')

f_contents = f.read()

f.close()

with open('test.txt','r') as f: # usefull for databases as well
	f_contents = f.read()

words = f_contents.split(' ')
word_count = len(words)
print(word_count)


'''
text = 'text to save\nNew line'

nameFile = 'saveText.txt'

saveFile = open(nameFile, 'w')
saveFile.write(text)
saveFile.write(text)
saveFile.close()

textAppend = '\nappended text'

appendFile = open(nameFile, 'a')
appendFile.write(textAppend)
appendFile.write('\n')
appendFile.write(textAppend)
appendFile.close()
'''
# nameFile = 'saveText.txt'

# r = 'r'
# readFile = open(nameFile, r).read()

# print(readFile)

# readFile = open(nameFile, 'r').readlines() #read into list

# print(readFile[0])

# nameFile = 'saveTextList.txt'
# saveFile = open(nameFile, 'w')
# #saveFile.write(readFile) #cannot save list, must be string
# #saveFile.close()

# for line in readFile:
# 	saveFile.write(line)


# saveFile.close()

#print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
#print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

