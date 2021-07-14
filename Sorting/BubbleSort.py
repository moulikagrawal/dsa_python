def bubbleSort(list):
   for i in range(len(list)-1):
      for j in range(len(list)-i-1):
         if(list[j] > list[j+1]):
            list[j],list[j+1] = list[j+1],list[j]
   return list

print(bubbleSort([3,6,1,0,9,2,8,4,7,5]))



