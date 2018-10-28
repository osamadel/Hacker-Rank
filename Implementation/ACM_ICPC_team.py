'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/acm-icpc-team/problem
'''

import math
import os
import random
import re
import sys

def sOR(str1, str2):
    count = 0
    for i in range(len(str2)):
        if not(str1[i] == '0' and str2[i] == '0'):
            count += 1
    return count

# Complete the acmTeam function below.
def acmTeam(topic):
    max_topics = 0
    maxs = []
    for i, t1 in enumerate(topic):
        for t2 in topic[i+1:]:
            topics = sOR(t1, t2)
            if topics >= max_topics:
                max_topics = topics
                maxs.append(topics)
    return [max_topics, maxs.count(max_topics)]



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
