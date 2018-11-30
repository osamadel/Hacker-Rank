'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
'''


import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    bdays = 0
    for num in range(i, j+1):
        reverse = int(str(num)[::-1].strip('0'))
        diff = abs(num - reverse)
        if diff % k == 0:
            bdays += 1
    return bdays

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
