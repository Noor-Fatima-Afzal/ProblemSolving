#!/bin/python3

# Problem Link: https://www.hackerrank.com/challenges/two-strings/problem
#
# Problem:
# Given two strings, determine if they share a common substring.
# A substring may be as small as one character.
# Return "YES" if they share a common substring, otherwise return "NO".

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    if set1 & set2:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()
        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
