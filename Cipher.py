
import math
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 

def main():
strng = 'this123456'
    L = len(strng)
    K = math.ceil(math.sqrt(L))
    M = K**2
    numast = (M-L)
    strng_index = 0
    #pad the string before posting into original array
    strng = strng + ("*" * numast)
 
    #create K x K matrix with all spaces via nested list
    matrix = [['' for x in range(K)] for y in range(K)]
    
    #fill from left to right with string characters
    for i in range(K):
        row = matrix[i]
        for j in range(K):
            row[j] = strng[strng_index]
            strng_index += 1
 
    #rotate matrix 90 degrees via reverse count row down the column
    rotated = [[matrix[j][i] for j in range(K-1, -1, -1)] for i in range(K)]
    print(rotated)
    #create blank string for output
    output = ''
    rotated_index = 0
    #read rotated matrix into output string directly
    for i in range(K):
        row = rotated[i]
        for j in range(K):
            output += row[j]
            rotated_index += 1 
    
    #replace all asterisks from output
    print(output)
    output = output.replace('*','')
    print(output)strng = 'this123456'
    L = len(strng)
    K = math.ceil(math.sqrt(L))
    M = K**2
    numast = (M-L)
    strng_index = 0
    #pad the string before posting into original array
    strng = strng + ("*" * numast)
 
    #create K x K matrix with all spaces via nested list
    matrix = [['' for x in range(K)] for y in range(K)]
    
    #fill from left to right with string characters
    for i in range(K):
        row = matrix[i]
        for j in range(K):
            row[j] = strng[strng_index]
            strng_index += 1
 
    #rotate matrix 90 degrees via reverse count row down the column
    rotated = [[matrix[j][i] for j in range(K-1, -1, -1)] for i in range(K)]
    print(rotated)
    #create blank string for output
    output = ''
    rotated_index = 0
    #read rotated matrix into output string directly
    for i in range(K):
        row = rotated[i]
        for j in range(K):
            output += row[j]
            rotated_index += 1 
    
    #replace all asterisks from output
    print(output)
    output = output.replace('*','')
    print(output)

if __name__ == "__main__":
  main()


