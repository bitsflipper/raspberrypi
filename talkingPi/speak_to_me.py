#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import subprocess
import time
import textwrap


Config=ConfigParser.ConfigParser()
try:
  Config.read('/home/pi/Scripts/talkingPi/alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

enabledSec=[]

for section in Config.sections():
  if section != 'main' and Config.get(section,'enabled')==str(1):
    try:
      enabledSec.append(getattr(__import__('get_'+section, fromlist=[section]),section))
    except ImportError:
      raise ImportError('Failed to load '+section)

count = 1

# key to getting text to speech
head = Config.get('main','head')+" "
tail = Config.get('main','tail')

# Combine all sections into a single string
enabled = (''.join(str(x) for x in enabledSec) + Config.get('main','end'))

# Print all enabled section for debug purposes if debug is enabled
if Config.get('main','debug') == str(1):
  print enabled
#raise Exception(wad)


# Use Google Translate to return an audio file (mp3) after translating the text
if Config.get('main','readaloud') == str(1):
  # strip any quotation marks
  enabled = enabled.replace('"', '').replace("'",'').strip()

  if Config.get('main','trygoogle') == str(1):
    # Google voice only accepts 100 characters or less, so split into chunks
    shorts = []
    for chunk in enabled.split('.  '):
      shorts.extend(textwrap.wrap(chunk, 100))


    # Send shorts to Google and return mp3s
    try:
      for sentence in shorts:
        sendthis = sentence.join(['"http://translate.google.com/translate_tts?tl=en&q=', '" -O /mnt/ram/'])
        print(head + sendthis + str(count).zfill(2) + str(tail))
        print subprocess.call (head + sendthis + str(count).zfill(2) + str(tail), shell=True)
        count = count + 1

      # Play the mp3s returned
      print subprocess.call ('mpg123 -g 100 -h 10 -d 11 /mnt/ram/*.mp3', shell=True)

    # festival is now called in case of error reaching Google
    except subprocess.CalledProcessError:
      print subprocess.call("echo " + enabled + " | festival --tts ", shell=True)
  
    # Cleanup any mp3 files created in this directory.
    print 'cleaning up now'
    print subprocess.call ('rm /mnt/ram/*.mp3', shell=True)
  else:
    print subprocess.call("echo " + enabled + " | festival --tts ", shell=True)
else:
  print enabled

