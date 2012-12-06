#!/usr/bin/env python
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
keystrokes=[]
clicks=[]
f=open('/home/brett/.workrave/historystats', 'r')
for line in f:
  if line[0]=='m':
    # Ignore 'm ' and '\n'
    clicks.append(int(line[2:-1].split(' ')[5]))
    keystrokes.append(int(line[2:-1].split(' ')[6]))
f.close()
# Data points
plt.plot(keystrokes, 'bo-')
plt.plot(clicks, 'r--')
# Best fit line
coeff=np.lib.polyfit(range(len(keystrokes)), keystrokes, 1)
p=np.lib.poly1d(coeff)
x_array=range(len(keystrokes))
plt.plot(x_array, p(x_array), 'g--')
# Labels
plt.ylabel("Count")
plt.xlabel("Days")
plt.legend(("Keystrokes", "Clicks"), "upper right")
plt.show()
