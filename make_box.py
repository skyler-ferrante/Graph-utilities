#!/bin/python3

'''
Create box plot,
taking data from stdin,
in the form of x
'''

import sys
import matplotlib.pyplot as plt

data = set()
for line in sys.stdin:
    try:
        x = int(line)
        data.add(x)
    except:
        print("Invalid line")
        sys.exit()

# showfliers=False, if too much data
plt.boxplot(data)
plt.show()
