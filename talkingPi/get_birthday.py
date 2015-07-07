#!/usr/bin/python
import time
import ConfigParser

#print int(time.strftime("%m%d"))

Config=ConfigParser.ConfigParser()
try:
  Config.read('/home/pi/Scripts/talkingPi/alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

birthday = 'null'

if int(time.strftime("%m%d")) == 529 :
  birthday = 'Tata'
if int(time.strftime("%m%d")) == 127 :
  birthday = 'Klarkee'
if int(time.strftime("%m%d")) == 407 :
  birthday = 'Danie'
if int(time.strftime("%m%d")) == 217 :
  birthday = 'Cherry'
if int(time.strftime("%m%d")) == 203 :
  birthday = 'Lola Aya'

print birthday

# reads out birthday
if birthday == 'null':
  birthday = ''
else:
  birthday = 'Today is ' + birthday + 's birthday.  ' 

if Config.get('main','debug') == str(1):
  print birthday


