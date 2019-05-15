#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    for i in range(0, len(arr) - 2):
        for j in range(i+1, len(arr) - 1):
            for k in range(j+1, len(arr)):
                if arr[k] == r*arr[j] and arr[j] == r*arr[i]:
                    count += 1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    # fptr.write(str(ans) + '\n')
    print(ans)

    # fptr.close()
