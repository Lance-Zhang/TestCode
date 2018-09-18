import serial
import pynmea2
from ISStreamer.Streamer import Streamer
import os
os.system("stty -F /dev/ttyS0 raw 9600 cs8 clocal -cstopb")

serialStream = serial.Serial("/dev/ttyS0", 9600, timeout=0.5)

# construct a streamer instance with information to append to or create 
# a bucket and an ini file location that contains the Initial State 
# Account Access Key.
#streamer = Streamer(bucket_name="GPS Tracker", ini_file_location="./isstreamer.ini")
streamer = Streamer(bucket_name="GPS Tracker")

try:
	while True:
		sentence = serialStream.readline()
		s1 = str(sentence,encoding="utf8")
		#print(s1)
		sentence = s1
		if sentence.find('GGA') > 0:
			data = pynmea2.parse(sentence)
			streamer.log("Satellite Count", data.num_sats)
			print("latitude: ",str(data.latitude))
			print("longitude: ",str(data.longitude))
##			if (data.num_sats >= 3):
##				streamer.log("Location", "{lat},{lon}".format(lat=data.latitude,lon=data.longitude))
##			if (data.num_sats >= 4):
##				streamer.log("Altitude ({unit})".format(unit=data.altitude_units), data.altitude)
except KeyboardInterrupt:
	streamer.close()
