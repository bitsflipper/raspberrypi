#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

subprocess.call('/usr/bin/python /home/pi/Scripts/talkingPi/shuffle.py "mpg123 -q" /home/pi/Audio/Songs .mp3', shell=True)
