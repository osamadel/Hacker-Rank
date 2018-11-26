'''
PROBLEM LINK:
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
'''

import math
import os
import random
import re
import sys


def build_leaderboard(scores):
    # current_score and last_score
    last_score = scores[0]
    # current_rank and last_rank
    rank = 1
    leaderboard = [[rank, last_score]]
    for score in scores[1:]:
        if score != last_score:
            # if the current score and last score are not equal, then both have the same ranking.
            rank += 1
            leaderboard.append([rank, score])
        else:
            leaderboard.append([rank, score])
        last_score = score
    return leaderboard


def insert_score(leaderboard, score, index):
    rank = leaderboard[index][0]
    leaderboard.insert(index, [rank, score])
    return rank


def find_rank(alice_score, leaderboard):        # How to traverse a list in reverse?!
    for i, score in enumerate(leaderboard):
        if alice_score >= score[1]:
            return i, insert_score(leaderboard, alice_score, i)
    return len(leaderboard) - 1, leaderboard[-1][0] + 1


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    alice_ranks = []
    leaderboard = build_leaderboard(scores)
    for alice_score in alice:
        last_index, rank = find_rank(alice_score, leaderboard)
        alice_ranks.append(rank)
        leaderboard = leaderboard[:last_index + 1]
    return alice_ranks


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)
    print('\n'.join(map(str,result)))

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
