#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    S_reminders = []
    for s_i in S:
        S_reminders.append(s_i % k)
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
