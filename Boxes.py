#!/bin/python3

#  File: Boxes.py

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes


def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
    #use template from class. lo = idx, and box list = a
    hi = len(box_list)
    #base case on last index
    if idx == hi:
        #instead of printing, we want to add to this 4th param, the list of all subsets
        all_box_subsets.append(sub_set)
        return
    #recursive case
    else:
        c = sub_set[:]
        sub_set.append(box_list[idx])
        #binary tree of both with the running subset (keep on adding) or saying no (add others but not this one)
        sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
        sub_sets_boxes(box_list, c, idx + 1, all_box_subsets)


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is

#so len of largest subset = largest size

def largest_nesting_subsets (all_box_subsets):
    
    #sort by size of subsets by # of elements, or len(subset)
    #https://www.w3schools.com/python/ref_func_sorted.asp
    subsets_largetosmall_n = sorted(all_box_subsets, key = len, reverse=True)

    #by definition, each param has to be less than the fit inside box AND this means volume MUST be less.
    
    #within this list of total subsets, sort each subset by the volume of the boxes in each one
    for i in range(len(subsets_largetosmall_n)):
        subsets_largetosmall_n[i].sort(key = lambda curr_box: curr_box[0] * curr_box[1] * curr_box[2])


    max_boxes = 0
    num_max_boxes_sets = 0
    
    
    for i in range(len(subsets_largetosmall_n)):
        #default
        does_nest = True
        #call on spec subset for each loop
        subset = subsets_largetosmall_n[i]

        #within the subset (:-1), go through boxes        
        for j in range(len(subset[:-1])):
            #fit is the nesting condition. if doesnt nest, break the tree algo
            if does_fit(subset[j], subset[j + 1]) == False: 
                does_nest = False
                break
            #if does nest, then loop case of counting
        if does_nest == True:
            
            if num_max_boxes_sets == 0:
                max_boxes = len(subset)
            #if current subset is less than the already IDd max one, we dont care, move on to next loop iteration
            if len(subset) < max_boxes:
                break
            #if all checks out, add this set to the number of max boxes
            else:
                num_max_boxes_sets += 1

    return max_boxes, num_max_boxes_sets

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
    # read the number of boxes
    in_file = open('boxes.in', 'r')
    line = in_file.readline()
    line = line.strip()
    num_boxes = int(line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range(num_boxes):
        line = in_file.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)

    # close the file
    in_file.close()

    '''
    # print to make sure that the input was read in correctly
    print(box_list)
    print()
    '''

    # sort the box list
    box_list.sort()

    '''
    # print the box_list to see if it has been sorted.
    print(box_list)
    print()
    '''

    # create an empty list to hold all subset of boxes
    all_box_subsets = []

    # create a list to hold a single subset of boxes
    sub_set = []

    # generate all subsets of boxes and store them in all_box_subsets
    sub_sets_boxes(box_list, sub_set, 0, all_box_subsets)

    # go through all the subset of boxes and only store the
    # largest subsets that nest in all_nesting_boxes
    largest_size, count = largest_nesting_subsets(all_box_subsets)

    # print the largest number of boxes that fit
    print(largest_size)

    # print the number of sets of such boxes
    print(count)

if __name__ == "__main__":
  main()
