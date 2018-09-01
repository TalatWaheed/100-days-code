# Python code to demonstrate the working of 
# typecode, itemsize, buffer_info()

import array
  
arr= array.array('i',[1, 2, 3, 1, 2, 5]) 
 
print ("The datatype of array is : ",end="")
print (arr.typecode)

print ("The itemsize of array is : ",end="")
print (arr.itemsize)
 
print ("The buffer info. of array is : ",end="")
print (arr.buffer_info())
