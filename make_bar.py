#!/bin/python3

'''
Create bar graph,
taking data from stdin,
in the form of x,label
'''

import sys
import matplotlib.pyplot as plt

labels = []
heights = []

for line in sys.stdin:
    line.rstrip()
    tokens = line.split(",")
    
    try:
        heights.append( float(tokens[0]) )
        labels.append(tokens[1])
    except:
        print("Invalid line")
        sys.exit()

# Set title to second command argument
if len(sys.argv) > 1:
    plt.title(sys.argv[1])

plt.bar(labels, heights)
plt.show()
