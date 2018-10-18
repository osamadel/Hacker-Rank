'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/repeated-string/problem
'''

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    repeats = n // len(s)
    remained_s = s[:n % len(s)] # + 1 ?!
    number_a = s.count('a') * repeats + remained_s.count('a')
    return number_a

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
