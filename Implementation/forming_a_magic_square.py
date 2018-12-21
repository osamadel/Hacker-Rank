'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/magic-square-forming/problem
'''

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
'''
Magic Matrix Formula: For a, b and c such that 0 < a < b < c − a and b ≠ 2a there exists
magic matrix :
c − b           c + (a + b)         c − a
c − (a − b)     c                   c + (a − b)
c + a           c − (a + b)         c + b
'''
def formingMagicSquare(s):
    c = s[1][1]
    return 0
    


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
