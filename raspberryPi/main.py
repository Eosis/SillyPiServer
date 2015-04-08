#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import requests
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

if len(sys.argv) != 2:
	print "./main.py <hostname>"
	exit(1)

hostname = sys.argv[1]

while True:
	r = requests.get("http://" + hostname + ":8080")
	print r.content

	if r.content == 'ON\r\n\r\n':
		GPIO.output(17, True)
		print "Turning LED on"
	else:
		GPIO.output(17, False)
		print "Turning LED off"

	time.sleep(5)