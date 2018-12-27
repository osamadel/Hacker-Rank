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
    sw = m + s - 1
    bad = sw % n
    bad = n if bad == 0 else bad
    return bad

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
