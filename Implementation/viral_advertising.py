'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/strange-advertising/problem
'''

import math
import os
import random
import re
import sys

def f(prev):
    return (prev // 2) * 3, prev // 2

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    culm_likes = 0
    shared = 5
    for i in range(n):
        shared, likes = f(shared)
        culm_likes += likes
    return culm_likes



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
