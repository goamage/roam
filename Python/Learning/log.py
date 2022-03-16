import sys
import time
import datetime
import os

startTime = datetime.datetime.now()

nameScript = 'get-ngavHostData'

pathDirRoot = os.path.dirname(__file__)
pathDirOutput = pathDirRoot + '\\output\\'
pathDirLog = pathDirRoot + '\\log\\'

nameFileLog = nameScript + '_log.txt'
pathFileLog = pathDirLog + nameFileLog

nameFileLogOld = nameScript + '_log_old.txt'
pathFileLogOld = pathDirLog + nameFileLogOld

nameFileDataCurrent = nameScript + '_current.csv'
pathFileDataCurrent = pathDirOutput + nameFileDataCurrent

nameFileDataPrevious = nameScript + '_previous.csv'
pathFileDataPrevious = pathDirOutput + nameFileDataPrevious


def log(data, s=0, e=0, f=1):

	if e == 1:
		excInfo = sys.exc_info()
		print(data)
		print(excInfo)
	else:
		print(data)
	
	if s == 1:
		separator = '/' * 50
		print(separator + '\n')
	
	if f == 1:  # write to file
		dateTimeNow = str(datetime.datetime.now())
		objFile = open(pathFileLog, 'a')	
		objFile.write(dateTimeNow + ' - ' + data + '\n')

		if e == 1:
			objFile.write(dateTimeNow + ' - ' + excInfo + '\n')

		if s == 1:
			objFile.write(dateTimeNow + ' - ' + separator + '\n')

		objFile.close()

#log(pathDirOutput)


def manageDataFile(fileCurrent, filePrevious):
	
	log('managing data files ..')
	if os.path.exists(fileCurrent) == True and os.path.exists(filePrevious) == True:
		log('.. deleting ' + filePrevious + ' ..')
		os.remove(filePrevious)
		log('.. deleting ' + filePrevious + ' done')
	
	if os.path.exists(fileCurrent) == True:
		log('.. renaming ' + fileCurrent + ' ..')
		os.rename(fileCurrent, filePrevious)
		log('.. renaming ' + fileCurrent + ' done')

		objFile = open(fileCurrent, 'w')
		objFile.close()
	
	log('managing data files done', s=1)

#manageDataFile(pathFileDataCurrent, pathFileDataPrevious)


def manageLogFile(fileLog, fileLogOld, daysBack):
	
	if os.path.exists(fileLog) == True:

		log('checking current log file: ' + fileLog + ' ..')

		timeNow = time.time()
		timeDaysBack = timeNow - daysBack * 86400
		log('.. date ' + str(daysBack) + ' + days back: ' + time.ctime(timeDaysBack))

		timeFile = os.stat(pathFileLog).st_ctime
		log('.. log file creation date: ' + time.ctime(timeFile))

		
		if timeFile < timeDaysBack:
			log('.. log file is older than ' + str(daysBack) + ' days')
			if os.path.exists(fileLogOld) == True:
				log('.. deleting ' + fileLogOld + ' ..')
				os.remove(fileLogOld)
				log('.. deleting ' + fileLogOld + ' done')
			
			log('.. renaming ' + fileLog + ' ..')
			os.rename(fileLog, fileLogOld)
			log('.. renaming ' + fileLog + ' done')
		else:
			log('.. log file is not older than ' + str(daysBack) + ' days')

		log('checking current log file: ' + fileLog + ' done', s=1)



manageDataFile(pathFileDataCurrent, pathFileDataPrevious)
manageLogFile(pathFileLog, pathFileLogOld, 30)



# startTime = datetime.datetime.now()

# #manageDataFile(pathFileDataCurrent, pathFileDataPrevious)
# #print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
# #print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

# timeNow = time.time()
# timeOld = timeNow - 7 * 86400 # minus 7 days

# log(str(timeNow))
# log(str(timeOld))
# log(time.ctime(timeNow))
# log(time.ctime(timeOld))



# log(str(os.path.getctime(pathFileLog)), s=1)


# log(time.ctime(timeNow))
# log(str(datetime.datetime.now()))
# log(time.ctime(os.path.getctime(pathFileLog)))

# log(str(os.stat(pathFileLog).st_ctime))

#time.sleep(3)



#log(str(datetime.timedelta(day=5)))




log('script run time: '+ str(datetime.datetime.now() - startTime), s=1)
