# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:22:03 2018

@author: CUHKSZ
"""

#This code sample uses requests (HTTP library)
import requests

params = {
    'access_token': '5ba9f4ae2b2b460a008bbd61|88cdda0cda9c3ececfa68371c2656673',
    'device_id': '70:ee:50:2e:e0:2a'
}
#  'device_id': '70:ee:50:2e:e0:2a'
# anemometer   03:00:00:01:9b:02
# indoor    70:ee:50:2e:e0:2a
# outdoor    02:00:00:2f:3b:4c

try:
    response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
    response.raise_for_status()
    data = response.json()["body"]
    print(data)
    print('\n')
    print(data['devices'][0]['modules'][1]['dashboard_data'])
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)
