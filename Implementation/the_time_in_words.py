'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/the-time-in-words/problem
'''

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
        minute_numbers = ["o' clock", 'one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine', 'ten',
                'eleven', 'twelve', 'thirteen', 'forteen', 'quarter',
                'sixteen', 'seventeen', 'eighteen', 'ninteen', 'twenty',
                'twenty one', 'twenty two', 'twenty three', 'twenty four',
                'twenty five', 'twenty six', 'twenty seven', 'twenty eight',
                'twenty nine', 'half']
    hours_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    hour_word = ''
    minute_word = ''
    if m <= 30:
        minute_word = minute_numbers[m]
        hour_word = hours_numbers[h - 1]
        pluralS = 'minutes' if m > 1 and m not in [15, 30] else 'minute'
        if m == 0:
            sentence = hour_word + " o' clock"
        elif m in [15, 30]:
            sentence = minute_word + ' past ' + hour_word
        else:
            sentence = minute_word + ' ' + pluralS + ' past ' + hour_word
    else:
        minute_word = minute_numbers[60 - m]
        hour_word = hours_numbers[h]
        pluralS = 'minutes' if m > 1 and m not in [15, 30] else 'minute'
        if 60-m in [15, 30]:
            sentence = minute_word + ' to ' + hour_word
        else:
            sentence = minute_word + ' ' + pluralS + ' to ' + hour_word
    return sentence

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
