def insertionSort(list):
   for i in range(1,len(list)):
      for j in range(i,0,-1):
         if(list[j] < list[j-1]):
            list[j],list[j-1] = list[j-1],list[j]
         else:
            break
   return list

print(insertionSort([-3,6,1,0,9,-2,8,4,7,5])) 