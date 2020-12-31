#Binary Tree now used for encryption
#another version of same BST concept (insert, search, etc)
#also creates encryption by documenting search instructions for each key in input

import sys

class Node (object):
	def __init__ (self, data):
		self.data = data
		self.lchild = None
		self.rchild = None
		# self.parent = None
		# self.visited = False

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
	def __init__ (self, encrypt_str):
		self.root = Node(None)
		self.string = encrypt_str
		encrypt_str = filter_st(encrypt_str)

		for char in encrypt_str:
			self.insert(char)	
		
  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
	def insert (self, ch):
		new_node = Node (ch)

		#empty tree
		if(self.root.data == None):
			self.root = new_node
			return

		else:
			#tries to find empty node
			current = self.root
			parent = self.root
			while (current != None):
				parent = current
				if (ch < current.data):
					current = current.lchild
				elif ch == current.data:
					break
				else:
					current = current.rchild
			
			# found location now insert node
			if (ch < parent.data):
				parent.lchild = new_node
			elif ch == parent.data:
				pass
			else:
				parent.rchild = new_node			
			

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
	def search (self, ch):
		#if num is root, return *!
		current = self.root
		if current.data == ch:
			return "*"

		#pathway
		line = ''
		#stays going through loop and adding directions.
		#adds to line as searching (not before)
		while (current.data != None):
			if (ch < current.data):
				line += '<'
				current = current.lchild
				
			elif ch > current.data:
				line += '>'
				current = current.rchild

			elif current.data == ch:
				return line

		#else return empty line, ch not found
		if current.data != ch:
			#resets line to zero, not all directions
			line = ''
			return line
			


  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
	def traverse (self, st):

		current = self.root

		#goes through string and follows arrows
		#until current = char or None
		for char in st:

			if char == "*":
				return self.root.data

			elif char == "<":
				current = current.lchild

			elif char == ">":
				current = current.rchild

			else:
				return ""
		
		return current.data 

		#example of in order traversal - left, center, right
		# if (aNode != None):
		#   self.in_order (aNode.lchild)
		#   print (aNode.data)
		#   self.in_order (aNode.rchild)

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
	def encrypt (self, st):
		#filter out
		st = filter_st(st)

		#search for number in tree, add to line
		line = ''
		for char in st:
			#print(char)
			#add = set of instructions for each char
			add = self.search(char)
			#print(add)
			
			#adding to final output
			line += add
			line += "!"
			#print(line)

		#return line missing the final ! point (delimiter not needed at end)
		return line[:-1]

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
	def decrypt (self, st):
		#separate by !, into list
		direct = st.strip().split('!')
		line = ""
		#for each set of directions, add to line
		for dset in direct:
			#find character for each traversal
			a = self.traverse(dset)
			#add to final output line to create decrypted word
			line += a
		
		return line

def filter_st(string):
		#filter out letters, return list of letters
		chars = []
		for char in string:

			#if a-z
			if ord(char) >= 97 and ord(char) <= 122:
				chars.append(char)
			
			#if space
			elif ord(char) == 32:
				chars.append(char)

			#if uppercase
			elif ord(char) >= 65 and ord(char) <= 90:
				chars.append(char.lower())

		return chars

def main():
	# read encrypt string
	line = sys.stdin.readline()
	encrypt_str = line.strip()
	# print(filter_st(encrypt_str))

	# create a Tree object
	the_tree = Tree (encrypt_str)

	# read string to be encrypted
	line = sys.stdin.readline()
	str_to_encode = line.strip()

	# print the encryption
	print (the_tree.encrypt(str_to_encode))

	# read the string to be decrypted
	line = sys.stdin.readline()
	str_to_decode = line.strip()

	# print the decryption
	print (the_tree.decrypt(str_to_decode))

if __name__ == "__main__":
	main()