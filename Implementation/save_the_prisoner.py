'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/save-the-prisoner/problem
'''

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    residual_sweets = m % n
    if residual_sweets + s - 1 > n:
        return residual_sweets + s - n - 1
    else:
        return residual_sweets + s - 1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
