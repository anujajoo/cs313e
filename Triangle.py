
#  File: Triangle.py


import sys

from timeit import timeit


#we want to go trhough ALL possible sums (exhaustive)
def brute_force(grid):
    curr_sum = [0]
    sum_create = []
    for i in range(len(grid)):
      sum_create.append(0)
    brute_test(0, 0, grid, curr_sum,  sum_create, len(grid))
    return curr_sum[0]

#treat row and column as from square
def brute_test(row, column, grid, curr_sum, working_array, length):
    #starting at 0,0 call of the grid (triangle made square with zeros)
    #go through all iterations THAT DO NOT INCLUDE the extra 0s 
    if (row < length  and column <= row) and grid[row][column] != 0:
        working_array[row] = grid[row][column]
        #
        if row < length-1:
            brute_test(row + 1, column, grid, curr_sum, working_array, length)
            brute_test(row + 1, column + 1, grid, curr_sum, working_array, length)
        else:
            working_sum = sum(working_array)
            if working_sum > curr_sum[0]:
                curr_sum[0] = working_sum



# returns the greatest path sum using greedy approach
# greedy = focus on the biggest values first and how to get them later
#choose path based on the next biggest number
#strictly different numbers?
def greedy (grid):
  greedy_sum = grid[0][0]
  col = 0
  for row in range(len(grid)-1):
    if grid[row + 1 ][col] > grid[row + 1][col + 1]:
      greedy_sum += grid[row + 1 ][col]
    else: 
      greedy_sum += grid[row + 1][col + 1]
      col +=1
  return greedy_sum

def recursive_solve(grid, row, col):
  if (row >= len(grid)-1):
    return grid[row][col]
  else:
    return grid[row][col] + max(recursive_solve(grid,row + 1, col), recursive_solve(grid,row + 1, col+1))


# returns the greatest path sum using divide and conquer (recursive) approach
  #break down into two triangles, short
def divide_conquer (grid):
  return recursive_solve(grid, 0, 0)

# returns the greatest path sum and the new grid using dynamic programming
#bottom up
#most similar to greatest sum path
#currently has a bug that makes it go on forever, ugh
def dynamic_prog (grid):
  n = len(grid)
  tri_grid = [[0 for i in range (n)] for j in range (n)]

  for row in range(n-1,-1,-1):
    for col in range(n-1,-1,-1):
      #0s aren't counted as grid
      if grid[row][col] == 0:
        continue 

      elif (row == n-1):
        #bottom row copied
        tri_grid[row][col] = grid[row][col]

      else: 
        #max cell between bottom nodes are added
        tri_grid[row][col] = max(grid[row][col] + tri_grid[row + 1][col], grid[row][col] + tri_grid[row+1][col+1])

  return tri_grid[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''


  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10 
  # print time taken using exhaustive search
  print("The greatest path sum through exhaustive search is")
  print(brute_force(grid))
  print("The time taken for exhaustive search in seconds is")
  print(times)
  
  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print("")
  print("The greatest path sum through greedy search is")
  print(greedy(grid))
  print("The time taken for greedy approach in seconds is")
  print(times)

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print("")
  print("The greatest path sum through recursive search is")
  print(divide_conquer(grid))
  print("The time taken for recursive search in seconds is")
  print(times)
  
  
  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  #print time taken using dynamic programming
  print()
  print("The greatest path sum through dynamic programming is")
  print(dynamic_prog(grid))
  print("The time taken for dynamic programming in seconds is")
  print(times)

  

if __name__ == "__main__":
  main()

