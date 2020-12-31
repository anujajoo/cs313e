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


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    v = 1
    toggle = False
    #use toggle to tell when v hits the turning point. exits loop returns v if so
    while toggle == False:
        if sum_series(v, k) < n:
            toggle = False
            v += 1
        else:
            toggle = True
    return v


def main(params):
    n = params[0]
    k = params[1]
    return linear_search(n, k)
    

if __name__ == "__main__":
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  inpt = sys.stdin.read().split()
  params = (int(inpt[0]), int(inpt[1]))
  fptr.write(str(main(params)))
  fptr.close()