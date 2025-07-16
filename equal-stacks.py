#!/bin/python3

# Problem Link: https://www.hackerrank.com/challenges/equal-stacks/problem
#
# Problem:
# Given three stacks of cylinders of different heights, remove cylinders from
# the top of the stacks to make all stacks equal in height. Find the maximum
# possible equal height.

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def build_stack(heights):
    stack = []
    total = 0
    for h in reversed(heights):
        total += h
        stack.append(total)
    return stack

def equalStacks(h1, h2, h3):
    st1 = build_stack(h1)
    st2 = build_stack(h2)
    st3 = build_stack(h3)

    while st1 and st2 and st3:
        top1 = st1[-1]
        top2 = st2[-1]
        top3 = st3[-1]

        if top1 == top2 == top3:
            return top1

        if top1 >= top2 and top1 >= top3:
            st1.pop()
        elif top2 >= top1 and top2 >= top3:
            st2.pop()
        else:
            st3.pop()

    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # FIX: Read all three sizes from one line
    n1, n2, n3 = map(int, input().strip().split())

    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
