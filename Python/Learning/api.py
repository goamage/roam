import requests as rq
import sys, os
import time
from datetime import datetime
startTime = datetime.now()
import json


def p(data, s=0):
	print(data)
	if s == 1:
		print('///////////////////////////////////////////////////////////\n')


# query = {'lat':'45', 'lon':'180'}
# response = rq.get('http://api.open-notify.org/iss-pass.json', params=query)


# https://www.youtube.com/watch?v=tb8gHvYlCFs
# https://httpbin.org/#/




# # timeout
# r = rq.get('https://httpbin.org/delay/4', timeout = 3)
# p(r)


# basic auth
#r = rq.get('https://httpbin.org/basic-auth/test/test', auth = ('test','test'))
auth = ('test','test')
r = rq.get('https://httpbin.org/basic-auth/test/test', auth = auth)
#p(r.text)
p(str(r.json()))

print(json.dumps(r.json(), indent=4, sort_keys=True))


#parsed = json.loads(r.json()) # to json
#print(json.dumps(str(r.json()), indent=4, sort_keys=True))


# # json parse
# data = {'username': 'test', 'password': 'test'}
# r = rq.post('https://httpbin.org/post', data = data)
# #r = rq.post('https://httpbin.org/post', data = data).json()
# p(r.json()['form'])

# rDict = r.json()
# p(rDict['form'])


# # post
# data = {'username': 'test', 'password': 'test'}
# r = rq.post('https://httpbin.org/post', data = data)
# p(r.text)
# p(r.json())


# # get
# params = {'page': 2, 'count': 25}
# #r = rq.get('https://httpbin.org/get?page=2&count=25')
# r = rq.get('https://httpbin.org/get', params = params)
# print(r.text) # check URL
# print(r.url) # source url
# #print(r.json())


# # download and save image
# # D:\Space\Silo\#3 TECH\Project\Code\Python\Learning
# r = rq.get('https://imgs.xkcd.com/comics/python.png')
# #print(r.content)

# with open('comic.png', 'wb') as f:
# 	f.write(r.content)


# # response basics
# r = rq.get('https://xkcd.com/353')
# #print(r)
# print(r.status_code)
# print(r.ok) # returns True for nonclient and server errors
# print(r.headers) # all response headers
# #print(dir(r))
# #print(help(r))
# #print(r.content) # good for images, in bytes
# #print(r.text) # in unicode


#time.sleep(2)
#execTime = (datetime.now() - startTime)
p((datetime.now() - startTime))


