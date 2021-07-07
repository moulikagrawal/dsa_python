import numpy

# def rotate90(array,n):
   # array1 = numpy.array([[2,3,4],[8,9,0],[4,8,2]])
   # for i in range(n):
   #    for j in range(n):
   #       array1[j][n-i-1] = array[i][j]
   # return array1

   # for i in range(n):
   #    for j in range(4):
   #       top = array[i][j]
   #       right = array[n-1][j]
   #       bottom = array[n-1][n-1]
   #       left = array[i][n-1]

   # return numpy.rot90()
      

# array = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# print(rotate90(array,n))

# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id1 = id(rec)
# del rec
# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id2 = id(rec)
# print(id1 == id2)

list1 = [1,2]
g = id(list1)
list1 = [7,8]
h = id(list1)

print(list1)