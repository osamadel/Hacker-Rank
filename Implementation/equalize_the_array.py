'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/equality-in-a-array/problem
'''

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    freq = {}
    for a in arr:
        if a not in freq:
            freq[a] = 1
        else:
            freq[a] += 1
    max = 0
    for f in freq:
        if freq[f] > max:
            max = freq[f]
    return len(arr) - max

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()