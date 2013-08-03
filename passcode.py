import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
zero = 17
one = 18
two = 22
red = 4
green = 24
gpio.setup(zero, gpio.IN)
gpio.setup(one, gpio.IN)
gpio.setup(two, gpio.IN)
gpio.setup(red, gpio.OUT)
gpio.setup(green, gpio.OUT)
gpio.setup(23, gpio.OUT)
password = "12120"
tempass = ""
oldtempass = tempass
correct = False
gpio.output(red, True)
while (correct == False):
  if (gpio.input(zero) == 0):
		tempass = tempass + "0"
	elif (gpio.input(one) == 0):
		tempass = tempass + "1"
	elif (gpio.input(two) == 0):
		tempass = tempass + "2"
	while (gpio.input(zero) == 0 or gpio.input(one) == 0 or gpio.input(two) == 0):
		gpio.output(23, True)
	gpio.output(23, False)
	if (len(tempass) == len(password)):
		if (tempass == password):
			print "Passcode correct!"
			gpio.output(red, False)
			time.sleep(0.5)
			gpio.output(green, True)
			time.sleep(0.5)
			gpio.output(green, False)
			time.sleep(0.5)
			gpio.output(green, True)
			time.sleep(0.5)
			gpio.output(green, False)
			time.sleep(0.5)
			gpio.output(green, True)
			time.sleep(0.5)
			gpio.output(green, False)
			time.sleep(0.5)
			correct = True
		else:
			print "Passcode wrong!"
			gpio.output(red, True)
			time.sleep(0.5)
			gpio.output(red, False)
			time.sleep(0.5)
			gpio.output(red, True)
			time.sleep(0.5)
			gpio.output(red, False)
			time.sleep(0.5)
			gpio.output(red, True)
			time.sleep(0.5)
			gpio.output(red, False)
			time.sleep(0.5)
			gpio.output(red, True)
			time.sleep(0.5)
			
			tempass = ""
	time.sleep(0.15)
	if (oldtempass != tempass):
		print tempass
		oldtempass = tempass
		
