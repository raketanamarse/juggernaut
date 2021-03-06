#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

servoPIN = 13

ygol = 72
yg = ygol/10
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # PWM with 50Hz
p.start(yg) # Initialization
p.ChangeDutyCycle(yg)
time.sleep(0.5)


with open("/home/pi/juggernaut/varfile13", "w") as f:
	f.write(str(ygol))
	f.close()


servoPIN = 12

ygol = 90
yg = ygol/10
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # PWM with 50Hz
p.start(yg) # Initialization
p.ChangeDutyCycle(yg)
time.sleep(0.5)


with open("/home/pi/juggernaut/varfile14", "w") as f:
	f.write(str(ygol))
	f.close()
