#!/bin/python3

# Problem Link: https://www.hackerrank.com/challenges/missing-numbers/problem
#
# Problem:
# Given two arrays, where the second array is a superset of the first but with some numbers
# possibly occurring more times, identify the numbers missing from the first array.
# Print the missing numbers in ascending order.

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    freq = defaultdict(int)

    # Count frequency in first array
    for num in arr:
        freq[num] += 1

    # Subtract frequency using second array
    for num in brr:
        freq[num] -= 1

    # Find numbers still with negative frequency (means they were missing in arr)
    missing = []
    for num in freq:
        if freq[num] < 0:
            missing.append(num)

    return sorted(missing)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())
    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)) + '\n')

    fptr.close()
