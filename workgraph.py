#!/usr/bin/env python
from datetime import datetime
def parseDateLine(line):
  data = line[2:-1].split(' ')
  start = datetime(2000+int(data[2][1:]), int(data[1]), int(data[0]), int(data[3]), int(data[4]))
  end = datetime(2000+int(data[7][1:]), int(data[6]), int(data[5]), int(data[8]), int(data[9]))
  return {'start': start, 'end': end}
def parseBreakLine(line):
  data = line[2:-1].split(' ')
def parseMiscLine(line):
  data = line[2:-1].split(' ')
f = open('stats/historystats', 'r')
for line in f:
  if line[0] == 'D':
    print parseDateLine(line)
  elif line[0] == 'B':
    parseBreakLine(line)
  elif line[0] == 'm':
    parseMiscLine(line)
f.close()
