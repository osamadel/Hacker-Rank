
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    number_ways = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            number_ways += 1
    return number_ways

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
