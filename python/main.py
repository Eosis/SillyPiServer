#!/usr/bin/python
import requests
r = requests.get('http://127.0.0.1:8080')
print r.content

if r.content == 'ON\r\n\r\n':
	print "Turning LED on"
else:
	print "Turning LED off"