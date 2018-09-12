import os
import pigpio
import RPi.GPIO as gpio
import time, sys

os.system('sudo killall -9 pigpiod')
os.system('sudo pigpiod')

pin = 17 # 4, 17, 27 , 22
dc =  0 # 0 ~ 100
servo = 27

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(pin,gpio.OUT,initial=False)


pi = pigpio.pi()
pi.set_servo_pulsewidth(servo,1500) #900~1700,  900 loosen, 1700 tighten

p = gpio.PWM(pin, 500) # channel, frequency
p.start(0)
#

p.ChangeDutyCycle(dc)

time.sleep(0.1)
a = input('please type any key. ')

p.stop()
gpio.cleanup()
