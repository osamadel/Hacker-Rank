'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/bon-appetit/problem
'''

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    anna_bill = bill.pop(k)
    anna_actual = sum(bill) // 2
    if anna_actual == b:
        return "Bon Appetit"
    else:
        return b - anna_actual

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    print(bonAppetit(bill, k, b))
