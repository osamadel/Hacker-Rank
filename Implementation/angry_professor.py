'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/angry-professor/problem
'''

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    ontime = 0
    for t in a:
        if t <= 0:
            ontime += 1
    if ontime >= k:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
        
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
