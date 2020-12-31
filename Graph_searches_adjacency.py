#  File: Graph.py

import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  def peek (self):
    return self.queue[0]

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))


class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

#edge class
#from, to, weight

#another data structure with adjacency list


class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph, sequential search
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (self.has_vertex (label)):
      return

    # add vertex to the list of vertices
    self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do a depth first search in a graph
  def dfs (self, v):
    #v is index of starting index
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us reset the flags, clean up
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do the breadth first search in a graph
  def bfs (self, v):
    #v is index of starting index
    #0. Create a Queue.
    theQueue = Queue ()

    # 1. Select a starting vertex. Make it the current vertex.
    #    Mark it visited.
    # mark the vertex v as visited
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)
    
    
    # visit all the other vertices according to breadth
    while (not theQueue.is_empty()):
      # get an adjacent unvisited vertex
      # 3. If you cannot carry out step 2 because there are no more
        #    unvisited vertices, remove a vertex from the queue (if
        #    possible) and make it the current vertex.
      u = self.get_adj_unvisited_vertex (theQueue.peek())
      if (u == -1):
        u = theQueue.dequeue()
      else:
        # 2. Visit an adjacent unvisited vertex (if there is one) in 
        #    order from the current vertex. Mark it visited and insert 
        #    it into the queue.
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theQueue.enqueue (u)
    
    # 4. Repeat steps 2 and 3 until the queue is empty.
    # the stack is empty, let us reset the flags, clean up
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
  
  # delete an edge from the adjacency matrix
  # delete two edges if the graph is undirected
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    #edge case if either aren't there
    if fromVertexLabel == -1 or toVertexLabel == -1:
      return

    #make weight into 0
    self.adjMat[fromVertexLabel][toVertexLabel] = 0
    self.adjMat[toVertexLabel][fromVertexLabel] = 0
    

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def delete_vertex (self, vertexLabel):
    #delete row
    index = self.get_index(vertexLabel)
    #edge case if either aren't there
    if index == -1:
      return
    else:
      self.adjMat.pop(index)

    #delete column, x index from every row
    for row in range (len(self.adjMat)):
      (self.adjMat[row]).pop(index)

    #delete vertex from list of vertexes
    if self.has_vertex(vertexLabel):
      self.Vertices.pop(index)



def main():
  #unweighted, undirected
  # create the Graph object
  cities = Graph()

  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int (line)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    city = line.strip()
    # print (city)
    cities.add_vertex (city)

  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int (line)
  # print (num_edges)

  # read each edge and place it in the adjacency matrix
  for i in range (num_edges):
    line = sys.stdin.readline()
    edge = line.strip()
    #print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.add_directed_edge (start, finish, weight)

  # # print the adjacency matrix
  # print ("\nAdjacency Matrix")
  # for i in range (num_vertices):
  #   for j in range (num_vertices):
  #     print (cities.adjMat[i][j], end = " ")
  #   print ()
  # print ()

  #START --------------

  # read the starting vertex for dfs and bfs
  line = sys.stdin.readline()
  start_vertex = line.strip()
  # print (start_vertex)

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)
  # print (start_index)

  # do the depth first search
  print ("\nDepth First Search" )
  cities.dfs (start_index)

  # test breadth first search
  print ("\nBreadth First Search" )
  cities.bfs (start_index)

  #input deletion edge
  line = sys.stdin.readline()
  verts = line.strip().split()
  start_vertex = verts[0]
  end_vertex = verts[1]
  #print ('delete:',start_vertex,'to',end_vertex)

  # test deletion of a edge
  print ("\nDeletion of an edge" )
  start_vertex = cities.get_index(start_vertex)
  end_vertex = cities.get_index(end_vertex)
  #print ('delete:',start_vertex,'to',end_vertex)
  cities.delete_edge (start_vertex,end_vertex)

  # print the adjacency matrix - edge deletion
  print ("\nAdjacency Matrix")
  for i in range (len(cities.adjMat)):
    for j in range (len(cities.adjMat)):
      print (cities.adjMat[i][j], end = " ")
    print ()

  #input deletion vertex
  line = sys.stdin.readline()
  line = line.strip()
  #print ('delete vertex:',line)

  # test deletion of Vertex
  print ("\nDeletion of a vertex" )
  cities.delete_vertex(line)

  #list of Vertices
  print ("\nList of Vertices" )
  nVert = len (cities.Vertices)
  for i in range (nVert):
      print(cities.Vertices[i])

  # print the adjacency matrix - vertex deletion
  print ("\nAdjacency Matrix")
  for i in range (len(cities.adjMat)):
    for j in range (len(cities.adjMat)):
      print (cities.adjMat[i][j], end = " ")
    print ()
  print ()
    
if __name__ == "__main__":
  main()

