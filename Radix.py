
#  File: Radix.py

#  Description: specific sorting algorithm for alphabet and numbers

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))


'''
for any set of strings, there is a different # of  digits based on the lengths
use combination of %10 and an increase
'''

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  #create queues for both digits and letters using ord and chr
  #add ot qlist as list of queues
  qlist = []#37 = 10 digs + 26 letters + 1 space because doesn't hit length
  for i in range(37):
    qlist.append(Queue())
  
  #letters 'a' starts at 97 and z ends at '122'
  #max length of string (# to search through)
  maxlen = len(a[0])
  for string in a:
    if len(string) > maxlen:
      maxlen = len(string)
  #now maxlen is the longest string length in input

  #NO LONGER PADDING
  # pad the strings so they're all the same length
  # for idx, string in enumerate(a):
  #   pad = maxlen - len(string)
  #   a[idx] =  ('0' * pad) + a[idx]


  #now have to loop through each time for the significant digit of the string length.
  radixed = a
  #loop from left to right for each character
  
  for pos in range(maxlen-1, -1, -1):
    #loop for each word for each character
    for string in radixed:
      #now we have a spec. 1-string to get the code for 
      if pos < len(string):  
        char = string[pos]
        #convert numbers 0-9 directly to int, and add to  queue, letters do some math
        if char.isdigit():
          qnum = int(char)
        elif char.isalpha():
          #ord of a is 97, so it will be right after 0-9 at Queue = 10. similarly, z is at end so 122 - 87 = 35.
          qnum = int(ord(char) - 87)
      else: #instead of padding just default a non existent position (empty space) to q_empty
        qnum = 0
      qlist[qnum].enqueue(string)
    
    #i have now enqueued all words for each iteration of the loop. going from right to left.
    #in order to dequeue
    radixed = []
    #loop through each iteration and going from right to left you now want to deq. for q in order (0 before 35 obviously)
    for q in qlist:
      while not q.is_empty():
        #add to final list in order
        radixed.append(q.dequeue())

  #this final list will be on the first possible sig digit with everything else in order (only some getting moved around)
  return radixed



def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  
  # print word_list
  # print (word_list)
 

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    
