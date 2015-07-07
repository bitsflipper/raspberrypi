#!/usr/bin/env python

# Program: shuffle.py
# Purpose: Play all music tracks in given directory in random order.
# Licence: Copyright (C) 2012 Raspberry Pi Foundation
#          Released under the GNU General Public Licence (GPL) Version 3
# Version: 0.1 2012/01/19
# Syntax: ./shuffle.py MusicPlayer MusicDirectory FileExtension
#         eg. "./shuffle.py mpg123 ~/Music .mp3"

import sys, os, glob, random

if len(sys.argv) != 4:
  print "Error: Wrong number of arguments."
  print "Syntax: ./shuffle.py MusicPlayer MusicDirectory FileExtension"
  exit(1)

print "Reading files in %s" % sys.argv[2]
music_files = []
for file in glob.glob(os.path.join(sys.argv[2], "*" + sys.argv[3])):
  music_files.append(file)

if len(music_files) == 0:
  print "Error: No matching files in that directory"
  exit(1)
else:
  print "%d tracks found." % len(music_files)

print "Shuffling tracks..."
shuffled_files = []
random.seed()
for t in range(len(music_files), 0, -1):
  track = random.randint(0, t - 1)
  shuffled_files.append(music_files[track])
  music_files.pop(track)

for track in shuffled_files:
  print "Playing track '%s'..." % track
  os.system(sys.argv[1] + " " + track)

print "Finished!"
exit(0)
