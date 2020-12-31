
#  File: Chess.py



import sys

class Queens (object):
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j],)
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  def recursive_solve (self, col, counter):
    if (col == self.n):
      #instead of returning something, just increase counter
      counter[0] += 1
    else:
      for i in range (self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          if (self.recursive_solve(col + 1, counter)):
            
            #same counter move
            counter[0] += 1
          self.board[i][col] = '*'
#no false, just doesnt add to counter
  # if the problem has a solution print the board
  def solve (self):
    counter = [0]
    # no need to take 2 params... just initialze counter in solve.
    self.recursive_solve(0, counter)
    #return the count and print in main call
    return counter[0]

def main():
  # read the size of the board
  in_file = open('chess.in', 'r')
  line = in_file.readline()
  line = line.strip()
  n = int(line)

  # create a chess board
  game = Queens (n)
  print(game.solve())
  # place the queens on the board and count the solutions

  # print the number of solutions
 
if __name__ == "__main__":
  main()

