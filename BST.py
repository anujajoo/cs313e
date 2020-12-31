

import sys

#Binary Tree code
#includes each traversal outputted in list format
#also includes comparison calculations + printing tree that is created (returning string)

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None
  # self.parent = None
  # self.visited = False

def height(node): 
    if node == None: 
        return 0  
    # Compute the depth of each subtree 
    else:
      left = height(node.lchild) 
      right = height(node.rchild) 
      
      h = max (left, right)

      return h + 1

class Tree (object):

  def __init__(self, data):
    self.root = None
    #initialize tree with reading in the data
    for i in data:
      self.insert(i)
      
    # insert data into the tree
  def insert (self, data):
    new_node = Node (data)

    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # found location now insert node
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # search for a node with given data
  def find (self, data):
    current = self.root
    while (current != None) and (current.data != data):
      if (data < current.data):
        current = current.lchild
      else:
        current = current.rchild
    return current
  
  def in_order(self, aNode, lst): # a should be an empty list
    if (aNode != None):
      self.in_order (aNode.lchild, lst)
      lst.append(aNode.data)
      self.in_order (aNode.rchild, lst)
      #return list of data in order increasing.
      return lst

  def pre_order(self, aNode, lst):
    if (aNode != None):
      lst.append(aNode.data)
      self.pre_order(aNode.lchild, lst)
      self.pre_order(aNode.rchild, lst)
      #return list of data in order left tree then right ones?.
      return lst

  # post order traversal - left, right, center
  def post_order (self, aNode, lst):
    if (aNode != None):
      self.post_order (aNode.lchild, lst)
      self.post_order (aNode.rchild, lst)
      lst.append (aNode.data)
      #return list of data in trees from left to right each level up the height.
      return lst


  # returns true if same exact nodes + in the same order. so check the post order traversal for this (same format, levels, etc)
  def is_similar (self, pNode):
    #check each traversal output and compare. if all are the same for all traversals, then TRUE. ELSE FALSE

    #inorder check  
    inl1 = self.in_order(self.root, [])
    inl2 = pNode.in_order(pNode.root, [])
    #pre order check
    prel1 = self.pre_order(self.root, [])
    prel2 = pNode.pre_order(pNode.root, [])
    #post order check
    postl1 = self.post_order(self.root, [])
    postl2 = pNode.post_order(pNode.root, [])

    #if all true, will return True. Else, False!
    return  inl1 ==  inl2 and prel1 == prel2 and postl1 == postl2
  
  # Prints out all nodes at the given level
  # Format: print all numbers in one line, numbers separated by a blank
  
  
  #to print nodes in order from left to right, have to realize the potential exponentiality of the binary tree
  # level 1 has 1 potential, 2 has 2, and then 3 has 4, 4 has 8 etx 
  #level n has 2^(n-1) potential nodes  to add to a list
  # so, must use a separate store of values to return from as we go left to right checking each pot. above node.
  def print_level (self, level): 
    
    #if empty tree, doesn't matter what level
    #if level more than height, doesnt matter (root = 1 hiehgt, heihgt of 1 = 2 levels, etc.)
    if (self.root == None) or level == 0:
      return ""
    
    curr_level = []
    curr_level.append(self.root)

    #loop through each level
    for lvl in range(1, level):
      #dynamically update current level until level is reached
      for curr_node in curr_level:
        #takes out first value in list
        curr_level = curr_level[1:]
        #then does left to right appending based on available subtrees
        if (curr_node.lchild != None) and (curr_node.rchild != None):
          curr_level.append(curr_node.lchild)
          curr_level.append(curr_node.rchild)
        
        elif (curr_node.lchild != None) and (curr_node.rchild == None):
          curr_level.append(curr_node.lchild)
        
        elif (curr_node.lchild == None) and (curr_node.rchild != None):
          curr_level.append(curr_node.rchild)
        
        #at end of each if sequence in loop, there is a different curr_level, moving onto next node.
                    
    printed_level = ""
    for i in curr_level:
      #convert nodes in list to data in string
      printed_level += (str(i.data) + ' ')
    #remove trailing space
    printed_level = printed_level.strip()  
    
    return printed_level

 #compare two ways of traversing and get max
  def get_height (self): 
    
    if (self.root == None) or (self.root.lchild == None and self.root.rchild == None):
      return 0
    #recursively call with root and then subtract 1 for root (path not nodes in path)
    return height(self.root) - 1   
  
  #total number of nodes are just what gets returned in the in order traversal
  def num_nodes (self):
    #empty tree = 0
    count = 0

    if (self.root == None):
      return count
    
    #just one node (None childs) = 1; both children are nonetype
    elif self.root.lchild == None and self.root.rchild == None:
      count = 1
      return count

    #now there are some type of subtrees. to get # nodes, get whats printed out (length) since traversals gave us a list
    #any traversal gives all values for that subtree, so
    
    #if only left subtree (and not right tree)
    elif self.root.lchild != None and self.root.rchild == None:
      left_nodes = len(self.in_order(self.root.lchild, []))
      #total count = left nodes + 1 for root
      count = left_nodes + 1
      return count
      
    
    #if only right subtree (and not left tree)
    elif self.root.lchild == None and self.root.rchild != None:
      right_nodes = len(self.in_order(self.root.rchild, []))
      #total count = right nodes + 1 for root
      count = right_nodes + 1
      return count
      
    
    #if both subtrees exist
    elif (self.root.lchild != None) and (self.root.rchild != None):
      left_nodes = len(self.in_order(self.root.lchild, []))
      right_nodes = len(self.in_order(self.root.rchild, []))
      count = left_nodes + right_nodes + 1
      return count


def main():
# Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line))  # converts elements into ints
    tree1 = Tree(tree1_input)
    tree2 = Tree(tree2_input)
    tree3 = Tree(tree3_input)


    #Test is_similar for every combination of trees
    #from assignment page: takes as input two binary search trees
    #returns true if the nodes have the same key values and are arranged in the same order and false otherwise
    
    #Below is the print ADJUSTED FOR THE TEST CASE GIVEN. CHANGE SHOULD BE BASED ON NEW INPUTS.
    print("Checking is_similar:")
    print("\nTree 1 is_similar to Tree 2: ", tree1.is_similar(tree2))
    print("Tree 1 is_similar to Tree 3: ", tree1.is_similar(tree3))

    print("Tree 2 is_similar to Tree 1: ", tree2.is_similar(tree1))
    print("Tree 2 is_similar to Tree 3: ", tree2.is_similar(tree3))

    print("Tree 3 is_similar to Tree 1: ", tree3.is_similar(tree1))
    print("Tree 3 is_similar to Tree 2: ", tree3.is_similar(tree2))

    #Lets assume that tree1 and tree2 are different
    #print different levels
    print("\nChecking print_level:\n")

    #print all 3 trees to check
    
    for level in range (1, tree1.get_height() + 1):
      print ("Tree 1 level", level, "is:", tree1.print_level(level))
    print("\n")
    for level in range (1, tree2.get_height() + 1):
      print ("Tree 2 level", level, "is:", tree2.print_level(level))
    print("\n")
    for level in range (1, tree3.get_height() + 1):
      print ("Tree 3 level", level, "is:", tree3.print_level(level))


    # #print heights
    print("\nChecking get_height:")
    print("\nTree 1 height is: ", tree1.get_height())
    print("Tree 2 height is: ", tree2.get_height())
    print("Tree 3 height is: ", tree3.get_height())

    #print num_nodes of each tree
    print("\nChecking num_nodes:")
    print("\nTree 1 # nodes: ", tree1.num_nodes())
    print("Tree 2 # nodes: ", tree2.num_nodes())
    print("Tree 3 # nodes: ", tree3.num_nodes())

if __name__ == "__main__":
    main()
