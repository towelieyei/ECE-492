#ECE-492
#Homework 3, Problem 3
#Taylor Harnagel

import time

print('This program translates single words into Pig Latin')
vowels = ['a','A','e','E','i','I','o','O','u','U','y','Y']

while True:
	x = raw_input('What word would you like to translate? ')
	l = len(x)
	print('length of x, l = '+str(l)) #for troubleshooting
		

	pig_latin = [] #this will be our translated word
	
	for i in range(0,l):	
		if x[0] == vowels[i]:
			aeiouy = True
		else:
			aeiouy = False
			
	if aeiouy == True:		
		pig_latin = x+str('hay') #This may not work...
	else:	
		pig_latin = x[1:]+x[0]+str('ay')
			
	print(str(x)+'is translated to '+str(pig_latin))
	time.sleep(0.5)

		#for i in range(x):
			#pig_latin = pig_latin[x[i-l]] #this may not work.
			#what i want is to flip the word		
