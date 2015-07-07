#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import subprocess

Config=ConfigParser.ConfigParser()
try:
  Config.read('/home/pi/Scripts/talkingPi/alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

subprocess.call('find '+ Config.get('main','musicfldr') + ' -name \'the_angelus.mp3\' | mpg123 -@ - -l 1 60', shell=True)
