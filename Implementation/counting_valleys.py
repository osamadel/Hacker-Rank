'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/counting-valleys/problem
'''

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude = 0
    sealevel = True
    valleys = 0
    for step in s:
        if step == 'U':
            altitude += 1
        else:
            altitude -= 1
        
        if altitude < 0 and sealevel:
            valleys += 1
            sealevel = False
        elif altitude > 0:
            sealevel = False
        elif altitude == 0:
            sealevel = True
    return valleys
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
