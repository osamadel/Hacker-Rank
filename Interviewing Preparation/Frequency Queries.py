#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    arr = {}
    output = []
    for q in queries:
        op = q[0]
        num = q[1]
        if op == 1:
            if not (arr.get(num, 0)):
                arr[num] = 1
            else:
                arr[num] += 1
        elif op == 2:
            if arr.get(num, 0):
                arr[num] -= 1
        elif op == 3:
            if int(num) in arr.values():
                output.append('1')
            else:
                output.append('0')
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(input().rstrip().split())

    ans = freqQuery(queries)

    fptr.write('\n'.join(ans))
    fptr.write('\n')

    fptr.close()
