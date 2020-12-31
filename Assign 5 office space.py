#!/bin/python3

import sys
 
def readinput():
    data = sys.stdin.readline()
    x, y = data.split()
    area_total = int(x) * int(y)
    num_employes = int(sys.stdin.readline().rstrip())
    workers = []
    for i in range(num_employes):
        worker = sys.stdin.readline().split()
        workers.append(worker)
   # print(workers)
   # print(num_employes)
   # print(x, y)
    return x, y, area_total , workers
 
 
 
def computations(data):
    w = int(data[0])
    h = int(data[1])  
    workers = data[3]
    office_space = [[0 for x in range(w)] for y in range(h)]
    #fills with 1s
    for i in workers:
        for row in range(int(i[2]), int(i[4])):
            for col in range(int(i[1]), int(i[3])):
                office_space[row][col] += 1 
    
    
    # finds claimed but also uncontested area
    for i in range(len(workers)):
        workers[i].append(0)
        for row in range(int(workers[i][2]), int(workers[i][4])):
            for col in range(int(workers[i][1]), int(workers[i][3])):
                if office_space[row][col] == 1:
                    workers[i][5] += 1
                
                    
    #find unallocated and contested
 
    contested = 0
    empty = 0 
    for i in range(len(office_space)):
        for j in range(len(office_space[i])):
            if office_space[i][j] > 1:
                contested += 1
            if office_space[i][j] == 0:
                empty += 1
  #  print(empty)
  #  print(contested)
  #  print(workers)
  #  print(office_space)
    return empty, contested, workers
 
def output(data, computed_data):
    workers = computed_data[2]
    unallocated = computed_data[0]
    contested = computed_data[1]
    total_area = data[2]
    print('Total' , total_area)
    print('Unallocated', unallocated)
    print('Contested', contested) 
    for i in range(len(workers)):
        print(workers[i][0], workers[i][5])
 
 
 
def main():
  # read the data
    data = readinput()
  # print the following results after computation
 #   print(data)
  # compute the total office space
  # compute the total unallocated space
    computated_data = computations(data)
   # print(computated_data)
    output(data, computated_data)
  # compute the total contested space
 
  # compute the uncontested space that each employee gets
    
    
 
if __name__ == "__main__":

