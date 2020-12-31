import math
#  File: MagicSquare.py

#  Description:
  '''Create a 1-D list of integers 1 through n2.
    Permute this list of integers.
    For each permutation check if this 1-D list is a magic square if converted to a 2-D list. If it is, then print the 1-D list.
    Stop when you have gone through all the permutations.'''


# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def make2D(list1D):
  n = int(math.sqrt(len(list1D)))
  list2d = []
  for i in range(n):
    row = []
    for j in range(n):
      row.append(j)
    list2d.append(row)

  return list2d
    



def is_magic (a):

    a2 = make2D(a)
    n = int(math.sqrt(len(a)))

    magic_sum = (n * (n**2 + 1)) / 2
    toggle = True

    running_sum = 0

    #checks rows
    for i in range(n):
    row = a2[i]
    #row checker
        for j in range(n):
            running_sum += row[j]
        #now check running sum for each row iteration
        if running_sum == magic_sum:
            toggle = True
        else:
            return False
        #reset running sum for next loop or next part of check
        running_sum = 0


    #checks columns
    for i in range(n):
    #col checker
        for j in range(n):
            running_sum += a2[j][i]
        #now check running sum for each column iteration
        if running_sum == magic_sum:
            toggle = True
        else:
            return False
        #reset running sum for next loop or next part of check
        running_sum = 0

    #checks diagonals
    diagonal_sum = 0
    for i in range(n):
        row = a2[i]
    #run through diagonal from left to right (0,0), (1,1), etc.
        for j in range(n):
            if i == j:
                diagonal_sum += row[j]
    #at this point have gotten full l2r diagonal, so check:
    if diagonal_sum == magic_sum:
        toggle = True
    else:
        return False

    #reset diagonal sum for reverse test
    diagonal_sum = 0
    for i in range(n):
        row = a2[i]
    #run through diagonal from right to left: ex 3x3 [0][2], [1][1], [2][0] ; i + j = n-1
        for j in range(n):
            if i + j == n-1:
                diagonal_sum += row[j]
    
    #at this point have gotten full r2l diagonal, so check:
    if diagonal_sum == magic_sum:
        toggle = True
    else:
        return False

    #at this point have tested each row, each column, and each diagonal. if toggle is still true, return it.
    #else the process should have returned False by now
    return toggle



# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# it stores all 1-D lists that are magic in the list all_magic
def permute ( a, idx, all_magic ):
  hi = len(a)
  if (idx == hi):
    all_magic.append(a)
  else:
    for i in range (idx, hi):
      a[idx], a[i] = a[i], a[idx]
      permute (a, idx + 1)
      a[idx], a[i] = a[i], a[idx]

#optimize by checking first n numbers if they equal 

def main():
  # read the dimension of the magic square
  in_file = open ('magic.in', 'r')
  line = in_file.readline()
  line = line.strip()
  n = int (line)
  in_file.close()

  '''
  # check if you read the input correctly
  print (n)
  '''

  # create an empty list for all magic squares
  all_magic = []

  # create the 1-D list that has the numbers 1 through n^2
  nums = []
  for i in range(n**2 + 1 ):
    nums.append(i)

  # generate all magic squares using permutation 
  permute( nums, 0, all_magic )

  # print all magic squares
  

if __name__ == "__main__":
  main()

