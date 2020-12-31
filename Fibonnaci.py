# File: Fibonacci.py

# Description: Assignment 10 submission -- finds # of times string p occurs in a binary fibonacci string sequence at position n



#recursive. we want to use memos tho since faster

import sys

#modif of the fib memo thing we wrote in class. now makes sure its all strings that get concatenated. same principle
def f_memo(n, memo):
    if n==0 or n==1:
        return memo[n]
    else:
        if n >= len(memo):
            f = str(f_memo(n-1, memo)) + str(f_memo(n-2, memo))
            memo.append(f)
            return f
        else:
            return memo[n]

#original recursive function. we wrote it but it doesnt work for higher up so it never is called
def f(n):
   if (n ==0 or n == 1):
       return n
   if (n >= 1):
       return str(f(n-1)) + str(f(n-2))

#loops through sequence using counters to find each instance        
def count_overlap(s, p):
   i = 0
   sequence_count = 0
   # Search through the string till
   # we reach the end of it
   while (i < len(s)):
       current_position = s.find(p, i)
 
       if current_position != -1:
           i = current_position + 1
           sequence_count += 1
 
       if (current_position == -1):
           break
   return sequence_count

#assigns memo with initial base case values as strings, and then reads input and calls on the count function. 
def main():
    memo = ['0', '1']
    n = sys.stdin.readline()
    n = int (n.strip())
    p = sys.stdin.readline()
    p = p.strip()

    s = f_memo(n, memo)

    count = count_overlap(s, p)

    print(count)
 
main()

