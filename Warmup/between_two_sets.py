import os
import sys
from math import gcd
from functools import reduce

#
# Complete the getTotalX function below.
#
def lcm(a, b):
    a = int(a)
    b = int(b)
    return a * b / gcd(a,b)

def lcms(numbers):
    return reduce(lcm, numbers)

def dividedByB(b, factor):
    for i in b:
        if i % factor != 0:
            return False
    return True

def getTotalX(a, b):
    # Getting the LCM for a
    LCM = lcms(a)
    bmax = max(b)
    # print(type(LCM))
    counter = 0
    multiplier = 1
    while LCM * multiplier <= bmax:
        if dividedByB(b, LCM*multiplier):
            counter += 1
        multiplier += 1

    return counter
        



if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    total = getTotalX(a, b)
    print(total)
    # f.write(str(total) + '\n')
    # f.close()
