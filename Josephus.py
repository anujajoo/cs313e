#  File: Josephus.py



import sys
class Link(object):
	# Constructor
	def __init__ (self, data, next = None):
		self.data = data
		self.next = next


class CircularList(object):
	# Constructor
	def __init__ (self): 
		self.first = None

	# Insert an element in the list
	def insert (self, item):
		# insert first
		new_link = Link(item)
		current = self.first

		# there is no link
		if (current == None):
			self.first = new_link
			new_link.next = new_link
			
			return

		while (current.next != self.first):
			current = current.next

		current.next = new_link
		new_link.next = self.first

	# Find the link with data
	def find (self, data):
		current = self.first

		while (current.data != data):
			current = current.next

		return current

  # Delete a link with a given key
	def delete (self, key):
		current = self.first
		previous = self.first
	
		# if list empty return none
		if (current == None):
			return None

		# while we haven't fully circled the list
		while (previous.next != self.first):
			previous = previous.next

		# (previous.next == self.first)
		# returned to where we started
		# clook for link with matching key value
		while (current.data != key):
			previous = current
			current = current.next

		#(current.data == key)
		if (self.first != self.first.next):
			# continue traversing
			self.first = current.next
		# (self.first == self.first.next)
		else:
			self.first = None

		# because you have deleted the link, now you need
		# to connect the previous link to the next link
		previous.next = current.next


	# Delete the nth link starting from the Link start 
	# Return the next link from the deleted Link
	def delete_after (self, start, n):
		curr = self.find(start)

		i = 1
		while i != n:
			curr = curr.next
			i +=1

		#loop all way to end
		
		#print the one to delete
		print(str(curr.data))
		
		#then delete
		self.delete(curr.data)

		#want to make sure were at new starting point so
		newstart = curr.next
		return newstart

	# Return a string representation of a Circular List
	def __str__ (self):

		#can't use for loop
		#but also must be two loops -- one for all 
		#must use while loop with break before 10 if ending (none)
		#dont want to print none either

		line = ""
		current = self.first

		# traverse until we reach the starting link
		while (current.next != self.first):
			line += str(current.data) + "/n "
			current = current.next

		return line

def main():
	# read number of soldiers
	line = sys.stdin.readline()
	line = line.strip()
	num_soldiers = int(line)

	# read the starting number
	line = sys.stdin.readline()
	line = line.strip()
	start_count = int(line)

	# read the elimination number
	line = sys.stdin.readline()
	line = line.strip()
	elim_num = int(line)

	circle = CircularList()

	#insert soldiers
	for i in range (1, num_soldiers + 1):
		circle.insert(i) 

	for i in range (1, num_soldiers + 1):
		#basically run the recursive back to the start count. starting start count is from the input -->
		#then whnen it runs again, want to be at start count + pos just moved
		start_count = circle.delete_after(start_count, elim_num)
		#print function built in do output is good
		start_count = start_count.data
	


main()