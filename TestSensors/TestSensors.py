# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 13:06:23 2018

@author: fahad

@contributor: Lianxin Zhang
"""

import time
import threading
# import RPi.GPIO as GPIO
import IMU
import sensor
# import matplotlib.pyplot as plt


if __name__ == "__main__":

    t1 = threading.Thread(target= IMU.IMU)
    t2 = threading.Thread(target= sensor.sensor)
    

    t1.start() # start thread 1
    t2.start() # start thread 2

##    t1.join() # wait for the t1 thread to complete
##    t2.join() # wait for the t2 thread to complete

    time.sleep(1)
    print('Connection closed!')
    
    
#-----------------------------------------------------------
