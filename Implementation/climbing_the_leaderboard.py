'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
'''

import math
import os
import random
import re
import sys
import time

def build_leaderboard_alt(scores):
    last_s = scores[0]
    leaderboard = [last_s]
    for s in scores[1:]:
        if s != last_s:
            leaderboard.append(s)
        last_s = s
    return leaderboard


def find_rank_alt(alice_score, leaderboard):
    l = leaderboard[:]
    i = len(l) // 2
    idx = i
    while True:
        if alice_score < l[i]:
            l = l[i:]
            i = len(l) // 2
            idx += i
        elif alice_score > l[i]:
            l = l[:i]
            i = len(l) // 2
            # idx -= (1 + i) if i%2 == 0 else i
            idx -= (len(l) - i)
        else:
            l = [l[i]]
            idx = i
        print('i=', i, '\tidx=', idx)
        if len(l) == 1:
            # idx+1 < len(leaderboard) and 
            if alice_score < leaderboard[idx]: idx += 1
            break
        elif len(l) == 0: break
    return idx


def build_leaderboard(scores):
    last_score = scores[0]
    rank = 1
    leaderboard = [[rank, last_score]]
    for score in scores[1:]:
        if score != last_score:
            rank += 1
            leaderboard.append([rank, score])
        else:
            leaderboard.append([rank, score])
        last_score = score
    return leaderboard


def find_rank(alice_score, leaderboard):
    leaderboard_length = len(leaderboard)
    for i in range(leaderboard_length):
        i_inv = leaderboard_length - 1 - i
        if alice_score < leaderboard[i_inv][1]:
            return i_inv, leaderboard[i_inv][0] + 1
        elif alice_score == leaderboard[i_inv][1]:
            return i_inv, leaderboard[i_inv][0]
    return 0, 1


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    # print('======================== LEADERBOARD ========================')
    # print('scores=', len(scores), '\nalice=', len(alice))
    # time.sleep(5)
    alice_ranks = []
    leaderboard = build_leaderboard(scores)
    for alice_score in alice:
        last_index, rank = find_rank(alice_score, leaderboard)
        # print('rank=', rank)
        alice_ranks.append(rank)
        leaderboard = leaderboard[:last_index + 1]
    return alice_ranks


def climbingLeaderboard_alt(scores, alice):
    # print('======================== LEADERBOARD ========================')
    # print('scores=', len(scores), '\nalice=', len(alice))
    # time.sleep(5)
    alice_ranks = []
    leaderboard = build_leaderboard_alt(scores)
    
    for alice_score in alice:
        # print('leaderobard:', leaderboard)
        index = find_rank_alt(alice_score, leaderboard)
        # print('rank=', index+1)
        alice_ranks.append(index+1)
        leaderboard = leaderboard[:index+1]
    return alice_ranks

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard_alt(scores, alice)
    print('\n'.join(map(str,result)))

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
