
import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maximum = minimum = scores[0]
    mostbreaks = 0
    leastbreaks = 0
    for s in scores[1:]:
        if maximum < s:
            maximum = s
            mostbreaks += 1
        if minimum > s:
            minimum = s
            leastbreaks += 1
    return mostbreaks, leastbreaks


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
