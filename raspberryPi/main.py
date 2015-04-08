#!/usr/bin/python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

import requests


while True:
	r = requests.get('http://192.168.0.5:8080')
	print r.content

	if r.content == 'ON\r\n\r\n':
		GPIO.output(17, True)
		print "Turning LED on"
	else:
		GPIO.output(17, False)
		print "Turning LED off"

	time.sleep(5)
