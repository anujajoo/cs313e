#!/bin/python3

import os
import re
import sys
import math

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    #need sum of infinite floor division
    #floor division returns 0 at f
    counter = 0
    term = v//(k**counter)
    summed_series = 0
    while term > 0:
        summed_series += term
        counter += 1
        term = v//(k**counter)
    return summed_series

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee

def binary_search (n: int, k: int) -> int:
    # use binary search here
    # what is list a of potential values of v?
    a = []
    for i in range(0, n+1):
        a.append(i)
    
    lo = 0
    hi = len(a) - 1
    while (lo <= hi):
        mid = (lo + hi) // 2
        if (sum_series(a[mid], k) < n):
            lo = mid + 1
        elif (sum_series(a[mid], k) > n):
            if sum_series(a[mid] - 1, k) < n:
                return a[mid]
            else:
                hi = mid - 1
        else:
            return a[mid]

def main(params):
    n = params[0]
    k = params[1]
    return binary_search(n,k)

if __name__ == "__main__":
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  inpt = sys.stdin.read().split()
  params = (int(inpt[0]), int(inpt[1]))
  fptr.write(str(main(params)))
  fptr.close()