 
# Enter your code here. Read input from STDIN. Print output to STDOUT. Do not change predefined function names or parameters
 
# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
 
def read_input():      #reads input from stdin and outputs a list with all tuples
    import sys
    numlines = sys.stdin.readline()
    
    tuples_list = []
    
    for line in sys.stdin.readlines():
        currline = line.split(' ')
        tuples_list.append((int(currline[0]), int(currline[1])))
    
    return tuples_list
 
#Create swap function for 2 elements in a list to switch order.
def swaplist(listname, pos1, pos2):
    listname[pos1], listname[pos2] = listname[pos2], listname[pos1]    
    return listname
 
def sort_tuples(tuples_list):
    n = len(tuples_list)
    endpos = n - 1
    
    for x in range(n):             #cycles through each index # from 0 to length
        for pos in range(endpos):  #cycles through tuple positions in list
                if tuples_list[pos][0] > tuples_list[pos+1][0]:  #compares first number in tuples  
                    swaplist(tuples_list, pos, pos+1)    #calls swap function
    return tuples_list
 
def merge_tuples(tuples_list, startpos =0):
    n = len(tuples_list)
    endpos = n -1
           #cycles through each index # from 0 to length
    for pos in range(startpos, endpos):  #cycles through tuple positions in list
        #if tuple 2's first number<tuple 1's second number, then the lists overlap. 
        if tuples_list[pos+1][0] < tuples_list[pos][1] and tuples_list[pos+1][1] < tuples_list[pos][1]:
            tuples_list[pos] = tuples_list[pos]
            del tuples_list[pos+1]
            #YES! Make a temporary list for each iteration to avoid repeat and then feed in
            #this is done by modifying startpos for each list (so delete works)
            #and then: returning this new list makes the next loop work the exact same way
            return merge_tuples(tuples_list.copy(), startpos = pos)
        elif tuples_list[pos+1][0] <= tuples_list[pos][1] and tuples_list[pos+1][1] >= tuples_list[pos][1]:
            tuples_list[pos] = (tuples_list[pos][0], tuples_list[pos+1][1])
            del tuples_list[pos+1]
            return merge_tuples(tuples_list.copy(), startpos = pos)
 
            
    return tuples_list
# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
 
def sort_by_interval_size(tuples_list, startpos =0):
    tuples_list.sort(key=lambda tuples_list: abs(tuples_list[0] - tuples_list[1]))
    return tuples_list
 
def main():
  # open file intervals.in and read the data and create a list of tuples
  tuples_list = read_input()
  
    ##sort list from first number in each tuple
  tuples_list = sort_tuples(tuples_list)
  # merge the list of tuples
  mergedlist = merge_tuples(tuples_list)
  # print the merged list
  print(mergedlist)
   ##right now this merged list has the right tuples and then ones in between,
   ##we need to figure out how to extract the right tuples ONLY
  # sort the list of tuples according to the size of the interval
  sortedlist = sort_by_interval_size(mergedlist)
  # print the sorted list
  print(sortedlist)
 
if __name__ == "__main__":
  main()
