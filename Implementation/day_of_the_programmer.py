'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/day-of-the-programmer/problem
'''
import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    elif (year < 1918 and year % 4 == 0) or (year > 1918 and ((year % 4 == 0 and year % 100 != 0)) or year%400 == 0):
        return "12.09." + str(year)
    else:
        return "13.09." + str(year)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
