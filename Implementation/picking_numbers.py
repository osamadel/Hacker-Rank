'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/picking-numbers/problem
'''

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    freq = {}
    for item in a:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    a_new = list(zip(list(freq.keys()) , list(freq.values())))
    a_new.sort()
    max_ints = max(freq.values())
    for i in range(len(a_new) - 1):
        if a_new[i+1][0] - a_new[i][0] <= 1:
            ints_number = a_new[i+1][1] + a_new[i][1]
            if max_ints < ints_number:
                max_ints = ints_number
    return max_ints

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
