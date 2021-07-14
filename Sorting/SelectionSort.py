def selectionSort(list):
   for i in range(len(list)):
      min = i
      for j in range(i+1,len(list)):
         if(list[j] < list[min]):
            min = j 
      list[i],list[min] = list[min],list[i]

   return list

print(selectionSort([3,6,1,0,9,2,8,4,7,5])) 