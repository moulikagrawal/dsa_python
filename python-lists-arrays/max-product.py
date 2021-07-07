import numpy as np

array = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13.14,35,16,27,58,19,21])

def maxProduct(array):
   # array.sort()
   # return array[-1]*array[-2]
   product = array[0]*array[1]
   for i in range(len(array)):
      for j in range(i+1,len(array)):
         if(array[i] * array[j] > product):
            product = array[i] * array[j]

   return product
   
print(maxProduct(array))