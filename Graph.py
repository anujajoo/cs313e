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


class Graph (object):
	def __init__ (self):
		self.Vertices = []
		self.adjMat = []

	# check if a vertex is already in the graph
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

	# get edge weight between two vertices
	# return -1 if edge does not exist
	def get_edge_weight (self, fromVertexLabel, toVertexLabel):
		weight = self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)]
		if (weight != 0):
			return (weight)
		return (-1)
	
	# get a list of immediate neighbors that you can go to from a vertex
	# return a list of indices or an empty list if there are none
	def get_neighbors (self, vertexLabel):
		neighbors = []
		vertex_index = self.get_index(vertexLabel)
		for i in range(len(self.Vertices[vertex_index])):
			if (self.Vertices[vertex_index][i] != 0):
				neighbors.append(self.Vertices[vertex_index][i])
		return (neighbors)
		
	# return an unvisited vertex adjacent to vertex v (index)
	def get_adj_unvisited_vertex (self, v):
		nVert = len (self.Vertices)
		for i in range (nVert):
			if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
				return i
		return -1

	# get a copy of the list of Vertex objects
	def get_vertices (self):
		for i in range(len(self.Vertices)):
			print(self.Vertices[i])

	# do a depth first search in a graph
	def dfs (self, v):
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

		# the stack is empty, let us rest the flags
		nVert = len (self.Vertices)
		for i in range (nVert):
			(self.Vertices[i]).visited = False
	
	# do a breadth first search in a graph starting at vertex v (index)
	def bfs (self, v):
		# 0. Create a Queue.
		bfs_queue = Queue ()

		# 1. Select a starting vertex. Make it the current vertex. Mark it visited.
		(self.Vertices[v]).visited = True
		print (self.Vertices[v])
		bfs_queue.enqueue (v)

		# 2. Visit an adjacent unvisited vertex (if there is one) in order from the current vertex. 
		# Mark it visited and insert it into the queue.
		# 3. If you cannot follow step 2, then if possible pop a vertex from the stack. 
		# Make it the current vertex.
		while (not bfs_queue.is_empty()):
			vertice_1 = bfs_queue.dequeue()
			vertice_2 = self.get_adj_unvisited_vertex(vertice_1)
			while (vertice_2 != -1):
				(self.Vertices[vertice_2]).visited = True
				print (self.Vertices[vertice_2])
				bfs_queue.enqueue (vertice_2)
				vertice_2 = self.get_adj_unvisited_vertex(vertice_1)

		# 4. Repeat steps 2 and 3 until the queue is empty.
		num_vertices = len (self.Vertices)
		for i in range (num_vertices):
			(self.Vertices[i]).visited = False

	# delete an edge from the adjacency matrix
	# delete a single edge if the graph is directed
	# delete two edges if the graph is undirected
	def delete_edge (self, fromVertexLabel, toVertexLabel):
		start = self.get_index(fromVertexLabel)
		end = self.get_index(toVertexLabel)
		self.adjMat[start][end] = 0
		self.adjMat[end][start] = 0

	# delete a vertex from the vertex list and all edges from and
	# to it in the adjacency matrix
	def delete_vertex (self, vertexLabel):
		vertex_index = self.get_index(vertexLabel)
		del(self.Vertices[vertex_index])
		del(self.adjMat[vertex_index])
		for i in range(len(self.Vertices)):
			del(self.adjMat[i][vertex_index])

	# shortest path with Dijkstra's algorithm
	def dijkstra_path (self, vertexLabel):
		nVert = len(self.Vertices)
		current_idx = self.get_index(vertexLabel)
		current = self.Vertices[current_idx]

		visited = set()
		visited.add(current)
    
    	# Each index in distances corresponds to the vertex at that index
    	#   in self.Vertices
    	# distances[i][0] : last visited vertex before "to vertex"
    	# distances[i][1] : "to vertex"
    	# distances[i][2] : total distance to vertex i

		distances = []
		for i in range(nVert):	
			row = [current, self.Vertices[i], float("inf")]
			distances.append(row)

		while len(visited) < nVert:
			for i in range(len(distances)):
				length = self.adjMat[current_idx][i]
				# distSoFar is distance from initial to current vertex
				if current.label == vertexLabel:
					distSoFar = 0
				else:
					distSoFar = distances[current_idx][2]
				# See if new path length is shorter than the previously found path
				if length > 0 and ((length + distSoFar) < distances[i][2]) and (distances[i][1] not in visited):
					distances[i][2] = length + distSoFar
					distances[i][0] = current
    			
			# Next vertex is the minimum path in distances that is not already used
			minEdge = distances[0]
			for i in range(1, len(distances)):
				if (distances[i][2] < minEdge[2]) and (distances[i][1] not in visited):
					minEdge = distances[i]
    			
			current = minEdge[1]
			current_idx = self.get_index(current.label)
			visited.add(current)
    		
    	# Print shortest using Dijkstra's 
		for i in distances:
			# Take out initial vertex
			if not i[2] == float("inf"):	
				print("Starting to", i[1], '-', i[2], end = '')
				if i[0].label != vertexLabel:
					print(" ( via", i[0], ')')
				else:
					print()

def main():
	# create the Graph object
	cities = Graph()

	# oepn the file for reading
	in_file = open ("graph.txt", "r")

	# read the number of vertices
	num_vertices = int ((in_file.readline()).strip())

	# read all the Vertices and add them the Graph
	for i in range (num_vertices):
		city = (in_file.readline()).strip()
		cities.add_vertex (city)

	# read the number of edges
	num_edges = int ((in_file.readline()).strip())

	# read each edge and place it in the adjacency matrix
	for i in range (num_edges):
		edge = (in_file.readline()).strip()
		edge = edge.split()
		start = int (edge[0])
		finish = int (edge[1])
		weight = int (edge[2])

		cities.add_directed_edge (start, finish, weight)

	# read the starting vertex 
	start_vertex = (in_file.readline()).strip()

	# get the index of the starting vertex
	start_index = cities.get_index (start_vertex)

	print("Original Adjacency Matrix")
	for i in range (num_vertices):
		for j in range (num_vertices):
			print (cities.adjMat[i][j], end = " ")
		print()
	print()

	# test depth first search
	print("Depth First Search")
	cities.dfs (start_index)
	print("")

	# test breadth first search
	print("Breadth First Search")
	cities.bfs (start_index)
	print("")

	# test deletion of an edge
	delete_edges = (in_file.readline()).strip().split()
	print("Delete edge between", delete_edges)
	cities.delete_edge(delete_edges[0], delete_edges[1])
	print("")

	# print the adjacency matrix
	print("Adjacency Matrix")
	for i in range (num_vertices):
		for j in range (num_vertices):
			print (cities.adjMat[i][j], end = " ")
		print()
	print()

	# test deletion of a vertex
	delete_vertex = (in_file.readline()).strip()
	print("Delete this vertex: ", delete_vertex)
	cities.delete_vertex(delete_vertex)
	print("")

	# print list of vertices
	print("List of Vertices")
	cities.get_vertices()
	print("")

	# print the adjacency matrix
	print ("Adjacency Matrix")
	num_vertices = len (cities.adjMat)
	for i in range (num_vertices):
		for j in range (num_vertices):
			print (cities.adjMat[i][j], end = " ")
		print()
	print()
		
	print("Dijkstra's Path:")
	cities.dijkstra_path(start_vertex)
	print()

if __name__ == "__main__":
	main()