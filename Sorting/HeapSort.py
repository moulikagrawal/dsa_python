def heapify(list,n,i):
   largest = i
   l = 2*i + 1
   r = 2*i + 2

   if(l<n and list[l] > list[largest]):
      largest = l

   if(r<n and list[r] > list[largest]):
      largest = r
   
   if(largest != i):
      list[i], list[largest] = list[largest], list[i]
      heapify(list,n,largest)

def heapSort(list):
   n = len(list)

   for i in range(int(n/2)-1,-1,-1):
      heapify(list,n,i)

   for i in range(n-1,-1,-1):
      list[i],list[0] = list[0],list[i]
      heapify(list,i,0)

   return list

print(heapSort([-3,6,1,0,9,-2,8,-4,7,-5]))