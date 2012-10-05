#!/usr/bin/env python
from datetime import date
import matplotlib.pyplot as plt
keystrokes=[]
clicks=[]
days=[]
f=open('/home/brett/.workrave/historystats','r')
for line in f:
  if line[0]=='D':
    # Ignore 'm ' and '\n'
    data=line[2:-1].split(' ')
    day=date(1900+int(data[2]),int(data[1])+1,int(data[0]))
    days.append(day)
  elif line[0]=='m':
    clicks.append(int(line[2:-1].split(' ')[5]))
    keystrokes.append(int(line[2:-1].split(' ')[6]))
f.close()
plt.plot(keystrokes,'bo-')
plt.plot(clicks,'r--')
avg=sum(keystrokes)/float(len(keystrokes))
plt.plot([0, len(days)], [avg, avg], 'g-')
plt.xticks(range(len(days)),days,rotation=45)
plt.ylabel("Count")
plt.xlabel("Date")
plt.legend(("Key presses","Mouse clicks"),"upper right")
plt.show()
