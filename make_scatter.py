#!/bin/python3

'''
Create scatter plot,
taking data from stdin,
in the form of x,y
'''

import matplotlib.pyplot as plt
import sys

# Hold multiple x values
xs = []

# Hold multiple y values
ys = []

for line in sys.stdin:
    tokens = line.split(",")

    try:
        x = float(tokens[0])
        y = float(tokens[1])
    except:
        print("Invalid line")
        sys.exit()
    
    xs.append(x)
    ys.append(y)

# Set title to second command argument
if len(sys.argv) > 1:
    plt.title(sys.argv[1])

plt.scatter(xs,ys)
plt.show()
