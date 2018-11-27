# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:58:08 2018

@author: CUHKSZ
"""


import os

os.system("raspistill -o keychain.jpg -t 2000")
# filename keychain.jpg
# wait for 2 sec

print('Photo is taken!')
