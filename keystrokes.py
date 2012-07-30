#!/usr/bin/env python
import matplotlib.pyplot as plt
keystrokes = []
f = open('/home/brett/.workrave/historystats', 'r')
for line in f:
  if line[0] == 'm':
    keystrokes.append(line[2:-1].split(' ')[6])
f.close()
plt.plot(keystrokes)
plt.show()
