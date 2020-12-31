
import sys


class Stack (object):
	def __init__(self):
		self.stack = []

	# add an item to the top of the stack
	def push(self, item):
		self.stack.append(item)

	# remove an item from the top of the stack
	def pop(self):
		return self.stack.pop()

	# check the item on the top of the stack
	def peek(self):
		return self.stack[-1]

	# check if the stack if empty
	def is_empty(self):
		return (len(self.stack) == 0)

	# return the number of elements in the stack
	def size(self):
		return (len(self.stack))


class Queue (object):
	def __init__(self):
		self.queue = []

	# add an item to the end of the queue
	def enqueue(self, item):
		self.queue.append(item)

	# remove an item from the beginning of the queue
	def dequeue(self):
		return (self.queue.pop(0))

	# check if the queue is empty
	def is_empty(self):
		return (len(self.queue) == 0)

	# return the size of the queue
	def size(self):
		return (len(self.queue))


class Vertex (object):
	def __init__(self, label):
		self.label = label
		self.visited = False

	# determine if a vertex was visited
	def was_visited(self):
		return self.visited

	# determine the label of the vertex
	def get_label(self):
		return self.label

	# string representation of the vertex
	def __str__(self):
		return str(self.label)


class Graph (object):
	def __init__(self):
		self.Vertices = []
		self.adjMat = []

	# check if a vertex is already in the graph
	def has_vertex(self, label):
		nVert = len(self.Vertices)
		for i in range(nVert):
			if (label == (self.Vertices[i]).get_label()):
				return True
		return False

	# given the label get the index of a vertex
	def get_index(self, label):
		nVert = len(self.Vertices)
		for i in range(nVert):
			if (label == (self.Vertices[i]).get_label()):
				return i
		return -1

	# add a Vertex with a given label to the graph
	def add_vertex(self, label):
		if (self.has_vertex(label)):
			return

		# add vertex to the list of vertices
		self.Vertices.append(Vertex(label))

		# add a new column in the adjacency matrix
		nVert = len(self.Vertices)
		for i in range(nVert - 1):
			(self.adjMat[i]).append(0)

		# add a new row for the new vertex
		new_row = []
		for i in range(nVert):
			new_row.append(0)
		self.adjMat.append(new_row)

	# add weighted directed edge to graph
	def add_directed_edge(self, start, finish, weight=1):
		self.adjMat[start][finish] = weight

	# add weighted undirected edge to graph
	def add_undirected_edge(self, start, finish, weight=1):
		self.adjMat[start][finish] = weight
		self.adjMat[finish][start] = weight

	# return an unvisited vertex adjacent to vertex v (index)
	def get_adj_unvisited_vertex(self, v):
		nVert = len(self.Vertices)
		for i in range(nVert):
			if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
				return i
		return -1

	def get_adj_vertex(self, v):
		nVert = len(self.Vertices)
		for i in range(nVert):
			if (self.adjMat[v][i] > 0):
				return i
		return -1

	# do a depth first search in a graph
	def dfs(self, v):
		# create the Stack
		theStack = Stack()

		# mark the vertex v as visited and push it on the Stack
		(self.Vertices[v]).visited = True
		print(self.Vertices[v])
		theStack.push(v)

		# visit all the other vertices according to depth
		while (not theStack.is_empty()):
			# get an adjacent unvisited vertex
			u = self.get_adj_unvisited_vertex(theStack.peek())
			if (u == -1):
				u = theStack.pop()
			else:
				(self.Vertices[u]).visited = True
				print(self.Vertices[u])
				theStack.push(u)

		# the stack is empty, let us rest the flags
		nVert = len(self.Vertices)
		for i in range(nVert):
			(self.Vertices[i]).visited = False

	# do the breadth first search in a graph
	# def bfs (self, v):
	#   return

	# determine if a directed graph has a cycle
	# this function should return a boolean and not print the result

	# ------------- START HERE -------------
	# return a list of vertices after a topological sort
	# this function should not print the list
	# has a recursive helper function
	def has_cycle(self):

		Graph_copy = Graph()

		#make brand new graph,go through and append each one
		# read the vertices to the list of Vertices
		for i in range(len(self.Vertices)):
			Graph_copy.add_vertex(self.Vertices[i].get_label)

		#print(Graph_copy.Vertices)
		
		# copy the adjacency matrix
		for row in range(len(self.Vertices)):
			for col in range(len(self.Vertices)):
				#print(row,col)
				Graph_copy.adjMat[row][col] = self.adjMat[row][col]
		
		# # print the adjacency matrix
		# print("\nAdjacency Matrix")
		# for i in range(len(Graph_copy.Vertices)):
		# 	for j in range(len(Graph_copy.Vertices)):
		# 		print(Graph_copy.adjMat[i][j], end=" ")
		# 	print()
		# print()

		#adjusted version of topo
		theQueue = Queue()
		
		while len(Graph_copy.Vertices) > 0:
			#print('loop')
			v_list = []
			for i in range(len(Graph_copy.Vertices)):
				#print('indegree', Graph_copy.in_degree(self.Vertices[i]), self.Vertices[i] )
				#print(i, len(Graph_copy.Vertices))
				
				#if in degrees = 0
				#true, append temp list
				if not(Graph_copy.no_deg(Graph_copy.Vertices[i])):
					v_list.append(Graph_copy.Vertices[i].get_label())
					#print(Graph_copy.Vertices[i])

			#if v_list is empty, return true
			if len(v_list) == 0:
				return True
			
			#sort temp, add queue, delete vertex
			v_list.reverse()
			for i in range(len(v_list)-1, -1, -1):
				theQueue.enqueue(v_list[i])
				Graph_copy.delete_vertex(v_list[i])		

		#doesn't have cycle at this point
		return False
		

	#returns in degree
	# def in_degree(self, vertex):
	# 	#col = self.adjMat[self.get_index(vertex.get_label())]

	# 	deg = 0
	# 	for row in range(len(self.Vertices)):
	# 		deg += self.adjMat[row][self.get_index(vertex.get_label())]

	# 	return deg
	
	# #does this vertex have a sucessor, aka any
	# # False deg = 0, True deg > 0
	def no_deg(self, vertex):

		for row in range(len(self.Vertices)):
			if (self.adjMat[row][self.get_index(vertex.get_label())]) != 0:
				return True

		return False

	def out_degree(self, vertex):
		return sum(self.adjMat[self.get_index(vertex.get_label())])
	
	# delete an edge from the adjacency matrix
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
			
	def toposort(self):

		theQueue = Queue()
		
		# 0. Determine the in_degree for all vertices. The in_degree is
		# the number of edges that are incident on that vertex. - given to us by matrix

		# 1. Remove the vertices that have an in_degree of 0 to a list and
		# remove the out going edges from those vertices. Sort the list
		# in a given order. Enqueue the vertices into a Queue and then 
		# update the in_degree of all remaining vertices.

		# 2. Repeat step 1 until there are no more vertices in the Graph.
		
		while len(self.Vertices) > 0:
			#print('loop')
			v_list = []
			for i in range(len(self.Vertices)):
				#print('indegree', self.in_degree(self.Vertices[i]), self.Vertices[i] )
				#print(i, len(self.Vertices))
				
				#if in degrees = 0
				#true, append temp list
				if not(self.no_deg(self.Vertices[i])):
					v_list.append(self.Vertices[i].get_label())
					#print(self.Vertices[i])
			
			#sort temp, add queue, delete vertex
			v_list.sort()
			v_list.reverse()
			for i in range(len(v_list)-1, -1, -1):
				theQueue.enqueue(v_list[i])
				self.delete_vertex(v_list[i])
					

		# 3. Dequeue the vertices and print.
		v_queue = []
		while not theQueue.is_empty():
			v_queue.append(theQueue.dequeue())
		
		#print(v_queue)

		return v_queue


def main():
	# create the Graph object
	theGraph = Graph()

	# read the number of vertices
	line = sys.stdin.readline()
	line = line.strip()
	num_vertices = int(line)

	# read the vertices to the list of Vertices
	for i in range(num_vertices):
		line = sys.stdin.readline()
		city = line.strip()
		#print(city)
		theGraph.add_vertex(city)
		
	# read the number of edges
	line = sys.stdin.readline()
	line = line.strip()
	num_edges = int(line)
	#print(num_edges)

	# read each edge and place it in the adjacency matrix
	for i in range(num_edges):
		line = sys.stdin.readline()
		edge = line.strip()
		#print(edge)
		edge = edge.split()
		start = edge[0]
		start = theGraph.get_index(start)
		finish = edge[1]
		finish = theGraph.get_index(finish)

		theGraph.add_directed_edge(start, finish, 1)
		

	# # print the adjacency matrix
	# print("\nAdjacency Matrix")
	# for i in range(num_vertices):
	# 	for j in range(num_vertices):
	# 		print(theGraph.adjMat[i][j], end=" ")
	# 	print()
	# print()

	# test if a directed graph has a cycle
	if (theGraph.has_cycle()):
		print("The Graph has a cycle.")
	else:
		print("The Graph does not have a cycle.")
		# test topological sort
		vertex_list = theGraph.toposort()
		print("\nList of vertices after toposort")
		print(vertex_list)

if __name__ == "__main__":
	main()