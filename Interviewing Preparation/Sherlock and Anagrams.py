#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    # generate substrings
    # for each substring
        # compute the frequency of each character
        # search for the same frequencies in array
        # if a match is found, increase the number of anagrams
        # else, store that frequency in array
    L = len(s)
    count = 0
    substr_freq = []
    for subsize in range(1,L+1):  # varying sizes of substrings
        for j in range(L-subsize+1):  # starting index
            found = False
            freq = [0] * 26
            substr = s[j : j+subsize]
            # print(substr)
            for char in substr:
                freq[ord(char) - 97] += 1 # increase the count of char in corresponding index at freq
            for f in substr_freq:
                # print([abs(x - y) for (x,y) in zip(f, freq)])
                if f == freq: # f and freq identical
                    count += 1
                    found = True
            # if not found:
            #     print("no freq match was found")
            substr_freq.append(freq)
            del freq
    return count
            



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        # fptr.write(str(result) + '\n')
        print(str(result))

    # fptr.close()
