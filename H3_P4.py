#ECE-492
#Homework 3, Problem 4
#Taylor Harnagel

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 23 # this pin triggers the sensor
GPIO.setup(trig,GPIO.OUT)
echo = 24	#input pin that reads the return signal from the sensor
GPIO.setup(echo,GPIO.IN)

print("This program uses echos to determine distance. In other words, echolocation")

try:
	while True:
		GPIO.output(trig,False)
		time.sleep(3)
		GPIO.output(trig,True)
		time.sleep(0.00001)
		GPIO.output(trig,False)
		
		while GPIO.input(echo)==0:
			start = time.time()

		while GPIO.input(echo)==1:
			stop = time.time()

		time_difference = stop - start

		distance = round(time_difference * 17150,2)
		
		cm_to_inch = distance * 0.393701
		
		print('Total distance is: '+str(cm_to_inch)+'inch(s)')	
	
finally:
	GPIO.cleanup()	
			

