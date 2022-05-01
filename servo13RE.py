#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

servoPIN = 13

with open("varfile13", "r") as f:
        stringIN = f.read(3)
        print(stringIN)
        print("------")
        INvar = 0
        INvar = (int(stringIN))
        print(INvar)
        log = 0
        if((INvar - 10) > 40):
                log = 1
                ygol = 0
                ygol = INvar - 10
                print(ygol)
                str(ygol)
                f.close()

                yg = 0.0
                yg = ygol/10
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(servoPIN, GPIO.OUT)
                p = GPIO.PWM(servoPIN, 50) # PWM with 50Hz
                p.start(yg) # Initialization
                p.ChangeDutyCycle(yg)
                time.sleep(0.5)


        with open("varfile13", "w") as f:
                if(log == 1):
                        log = 0
                        f.write(str(ygol))
                        p.stop()
                        GPIO.cleanup()
                else:
                        f.write(stringIN)
                        f.close()
