'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/migratory-birds/problem
'''
import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    f = 5 * [0]
    for a in arr:
        f[a-1] += 1
    return f.index(max(f)) + 1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
