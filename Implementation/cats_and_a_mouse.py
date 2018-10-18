'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
'''
import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    catA_d = abs(x - z)
    catB_d = abs(y - z)
    if catA_d < catB_d:
        return 'Cat A'
    elif catB_d < catA_d:
        return 'Cat B'
    else:
        return 'Mouse C'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
