#!/usr/bin/env python
from datetime import datetime
import matplotlib.pyplot as plt

def parseDateLine(line):
  data = line[2:-1].split(' ')
  start = datetime(1900+int(data[2]), int(data[1]), int(data[0]), int(data[3]), int(data[4]))
  end = datetime(1900+int(data[7]), int(data[6]), int(data[5]), int(data[8]), int(data[9]))
  return {'start': start, 'end': end}

def parseBreakLine(line):
  data = line[2:].split(' ')[:-1]
  return {}#'type': data[0], 'prompted': data[2]}

def parseMiscLine(line):
  data = line[2:-1].split(' ')
  return {'keystrokes': data[6]}

days = []
keystrokes = []

f = open('stats/historystats', 'r')
for line in f:
  if line[0] == 'D':
    days.append(parseDateLine(line))
  #elif line[0] == 'B':
    #day.update(parseBreakLine(line))
  elif line[0] == 'm':
    keystrokes.append(parseMiscLine(line))
f.close()

print days
#plt.plot(clicks, 'r--')
#plt.plot(keystrokes, 'bo-')
#plt.show()
