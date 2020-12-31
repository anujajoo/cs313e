#  File: Reducible.py



import math

def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True
  # Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise

#prime number bigger than n
def bigger_prime(n):
  while (is_prime(n) == False):
    n +=1
  
  return n


# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  #hash code of s, constant
  #return constant - hashcode
  return const - hash_word(s,const)
  

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  n = len(hash_table)
  key = hash_word(s,n)
  if (hash_table[key] == ""):
    hash_table[key] = s
  else:
    #key = (key + step_size) % len(hash_table)
    #choose prime number, and be consistent on code, 13 or 17 only
    step = step_size(s,13)
    while (hash_table[key]  != ""):
      key = (key + step) % n
    hash_table[key] = s

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  #look through each index to find word
  #index i through len(hash_table)
  #similar to insert, probe until find
  key = hash_word(s,len(hash_table))
  step = step_size(s,13)
    #key = (key + step_size) % len(hash_table)
    #choose prime number, and be consistent on code, 13 or 15 onl
  while (hash_table[key]  != ''):
    if hash_table[key] == s:
      return True
    else:
      key = (key + step) % len(hash_table)
  return False


  #recursive, backtracking looking for if a word is made for taking away a letter
  # is it in our dictorionary?  
  #basecase if length of s is 1 and a,i,o
    #is s inside hash_table for valid word
  #if s is inside hash_memo, reducable, returns immediately

  #if len = 1, check if a, i, or o
  #if in memo, then return true
  #if not in table then return false
  #loop over string, make temp string, call is_reducible 
  #if temp isn't in memo, if true

  #if reducable, add into hash_memo 
    #temp string, loop over string

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  if len(s) == 1:
    if s == 'a' or s == 'i' or s == 'o':
      return True
    else:
      return False

  if not find_word (s, hash_table):
    return False
  if find_word (s, hash_memo):
    return True


  for i in range(len(s)):
    temp = s[:i] + s[i + 1:]
    if is_reducible (temp, hash_table, hash_memo):
      if not find_word(temp, hash_memo):
        insert_word(temp,hash_memo)
      return True
  return False


def main():
  # create an empty word_list
  word_list = []

  # open the file words.txt
  f = open("words.txt", "r")

  # read words from words.txt and append to word_list
  for line in f:
    word_list.append(line.strip())

  # close file words.txt
  f.close()

  
  # find length of word_list
  length = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  primeNum = bigger_prime(2 * length)

  # create an empty hash_list
  hash_list = ["" for i in range(primeNum)]
  # populate the hash_list with N blank strings
 

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for word in word_list:
    insert_word(word ,hash_list)
    


  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  m = bigger_prime(int(.2 * len(word_list)))
  # populate the hash_memo with M blank strings
  hash_memo = ['' for i in range(m)]

  # create an empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  for word in word_list:
    if len(word) == 10:
      if is_reducible(word,hash_list, hash_memo):
        reducible_words.append(word)

  # find words of length 10 in reducible_words
  # long_list = get_longest_words (reducible_words)
  # print(long_list)

  # print the words of length 10 in alphabetical order
  # one word per line
  for word in reducible_words:
    print(word) 
  

if __name__ == "__main__":
  main()
