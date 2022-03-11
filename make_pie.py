#!/bin/python3

'''
Create pie graph,
taking data from stdin,
in the form of x,label
'''

import sys
import matplotlib.pyplot as plt

labels = []
size = []

for line in sys.stdin:
    line.rstrip()
    tokens = line.split(",")
    
    try:
        size.append( float(tokens[0]) )
        labels.append(tokens[1])
    except:
        print("Invalid line",line)
        sys.exit()

# Set title to second command argument
if len(sys.argv) > 1:
    plt.title(sys.argv[1])

plt.pie(size, labels=labels)
plt.show()
