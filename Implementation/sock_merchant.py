'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/sock-merchant/problem
'''
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors = {}
    for c in ar:
        if c not in colors:
            colors[c] = 1
        else:
            colors[c] += 1
    pairs = 0
    for c in colors:
        pairs += colors[c] // 2
    return pairs

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
