#print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
#print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

timeNow = time.time()
timeOld = timeNow - 7 * 86400 # minus 7 days

log(str(timeNow))
log(str(timeOld))
log(time.ctime(timeNow))
log(time.ctime(timeOld))



log(str(os.path.getctime(pathFileLog)), s=1)


log(time.ctime(timeNow))
log(str(datetime.datetime.now()))
log(time.ctime(os.path.getctime(pathFileLog)))

log(str(os.stat(pathFileLog).st_ctime))

#time.sleep(3)