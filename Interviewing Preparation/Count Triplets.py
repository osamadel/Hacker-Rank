#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    keys = []
    values = []

    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[j] / r == arr[i]:
                keys.append(i)
                values.append(j)
    
    print(keys)
    print(values)
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            if values[i] == keys[j]:
                count += 1

    # for i in range(0, len(arr) - 2):
    #     for j in range(i+1, len(arr) - 1):
    #         if arr[j] / r == arr[i]:
    #             for k in range(j+1, len(arr)):
    #                 if arr[k] / r == arr[j]: 
    #                     count += 1
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
