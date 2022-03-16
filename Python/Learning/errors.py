

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
nameFile = 'saveText.txt'

readFile = open(nameFile, 'r').read()

print(readFile)

readFile = open(nameFile, 'r').readlines() #read into list

print(readFile[0])

nameFile = 'saveTextList.txt'
saveFile = open(nameFile, 'w')
#saveFile.write(readFile) #cannot save list, must be string
#saveFile.close()

for line in readFile:
	saveFile.write(line)


saveFile.close()

