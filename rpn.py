#!/bin/python3

#Postfix, prefix, rpn, etc
'''
* Given a valid RPN expression how do you evaluate it

* Parse the RPN expression (go through the expression token by token)

* If the token is an operand push the operand on the stack

* If the token is an operator 
  - pop the stack twice
  - apply the operator to those operands 
  - push the result on the stack

* When you finish parsing there should be only one number in the stack. 
  Pop the stack. That is your answer.

* Code to evaluate RPN expressions stored in a file called rpn.txt
'''

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item on the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def is_empty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

def operate (oper1, oper2, token):
  expr = str(oper1) + token + str(oper2)
  return eval (expr)

def rpn (s):
  theStack = Stack()

  operators = ['+', '-', '*', '/', '//', '%', '**']

    #make a list of each thing in the input string  
  tokens = s.split()

  for item in tokens:
    if (item in operators):
      oper2 = theStack.pop()
      oper1 = theStack.pop()
      theStack.push (operate (oper1, oper2, item))
    else:
      theStack.push (item)

  return theStack.pop()

  
def main():
  in_file = open ("rpn.txt", "r")
  for line in in_file:
    line = line.strip()
    value = rpn (line)
    print (line, " = ", value)
  in_file.close()

main()

# class Stack(object):
#     def __init__ (self):
#         self.stack = []

#     #add item to top of stack
#     def push (self, item):
#         self.stack.append(item)

#     #remove an item, call it pop
#     def pop (self):
#         return self.stack.pop()

#     #check item on top but dont remove
#     def peek (self):
#         return self.stack[-1]

#     #check if it is empty
#     def is_empty (self):
#         return len(self.stack) == 0

#     #return elements in stack
#     def size (self):
#         return len(self.stack)

# def operate(operand1, operand2, token):
#     expr = str(operand1) + token + str(operand2)
#     return eval(expr)


# def rpn (s):
#     tstack = Stack()

#     operators = ['+', '-', '*', '/', '%', '//', '**']

#     #makes list of input postfix string into separate tokens
#     tokens = s.split()

#     for item in tokens:
#         if (item in operators):
#             #if operator in the reading of string, pop the stack twice and apply operator
#             operand1 = tstack.pop()
#             operand2 = tstack.pop()
#             tstack.push(operate(operand1, operand2, item))
#         else:
#             tstack.push(item)
    
#     return tstack.pop()

# def main():
#     in_file = open("rpn.txt", "r")
#     for line in in_file:
#         line = line.strip()
#         value = rpn(line)
#         print (line, '=', value)
#     in_file.close()

# main()