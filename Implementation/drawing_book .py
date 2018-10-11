'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/drawing-book/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n % 2 == 0 and n > 4:
        return min(p // 2, (n-p+1) // 2)
    else:
        return min(p // 2, (n-p) // 2)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
