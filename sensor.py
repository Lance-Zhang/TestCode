# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:05:38 2018

@author: CUHKSZ
"""

import time
#from collections import deque
from ina219 import INA219
from ina219 import DeviceRangeError


def sensor():
    
    Shunt_OHMS = 0.085 # For this sensor it is 0.1 ohm

    try:
        print('Starting Current Sensor')
        print('Collecting Sensor Values...')
        start = time.time() # Start Time
        
        #global DataPoints
        #DataPoints = deque(maxlen=None) # Creating Array of datatype Deque to store values

        a = 0.9664 # Regression Fitting Parameter
        b = 0.0285 # Regression Fitting Parameter
        
        ina = INA219(Shunt_OHMS) # Auto Gain
        
        while True:
            try:
                ina.configure()
                break
            except:
                print('Cannot configure ina219!')

        print('Current Sensor Configured Successfully')
        while True:            
        
            print('Bus Voltage: %.3f V' % ina.voltage())
            
            try:
                #print('Bus Current: %.3f mA' % ina.current())
                #print('Power: %.3f mW' % ina.power())
                print('1')
                currentvalue = round((a*ina.current())+b) # Rounding off values to nearest integer
##                print('2')
                voltagevalue = float('{0:.1f}'.format(ina.voltage())) # Floating point up to one decimal point
                powervalue = round(currentvalue*voltagevalue)
                timevalue = float('{0:.1f}'.format(time.time()-start)) # Elapsed time in Seconds with 1 decimal point floating number 
        
                #DataPoints.append([timevalue, currentvalue, voltagevalue, powervalue]) # Updating DataPoints Array
                print('Current value is:  ',currentvalue)
                
            except DeviceRangeError:
                print('Device Range Error')

            time.sleep(0.5) # Reading value after 0.5 second
        
    except:        
        print('Exception Occurred, Current Sensor Stopped \n')

##    with open(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'.txt','w') as f:
##        f.write(str(currentvalue)+' '+str(voltagevalue)+' '+str(powervalue)+' '+str(timevalue)+'\n')

    print('Sensor Stopped!\n')
#------------------------------------------------

#sensor()