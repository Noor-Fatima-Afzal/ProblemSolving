#!/bin/python3

# Problem Link: https://www.hackerrank.com/challenges/array-left-rotation/problem
#
# Problem:
# A left rotation operation on an array shifts each of the array's elements
# 1 unit to the left. Given an integer d, rotate the array that many times.
# Return the updated array.

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateLeft(d, arr):
    n = len(arr)
    d %= n  # In case d > n

    # Reverse the entire array
    reverse(arr, 0, n - 1)
    # Reverse the last n - d elements
    reverse(arr, 0, n - d - 1)
    # Reverse the first d elements (which were originally the last d)
    reverse(arr, n - d, n - 1)

    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)) + '\n')

    fptr.close()
