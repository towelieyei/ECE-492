#ECE-492
#Homework 3, Problem 1
#Taylor Harnagel

import time
import RPi.GPIO as GPIO

#Use Boardcom-chip
GPIO.setmode(GPIO.BCM)

#GPIO pin assignment and setup
LED_pins = [4,17,18,27]
GPIO.setup(LED_pins, GPIO.OUT)


try:
	while 1:
		#LED1
		GPIO.output(4,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(4,GPIO.LOW)
		#LED2
		GPIO.output(17,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(17,GPIO.LOW)
		#LED3
		GPIO.output(18,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(18,GPIO.LOW)
		#LED4
		GPIO.output(27,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(27,GPIO.LOW)
		time.sleep(0.1)
		#LED3
		GPIO.output(18,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(18,GPIO.LOW)
		#LED2
		GPIO.output(17,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(17,GPIO.LOW)
					
finally:
	print("Cleaning up")
	GPIO.cleanup()
