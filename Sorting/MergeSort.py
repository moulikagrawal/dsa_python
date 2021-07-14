def merge(list,l,m,r):
   n1 = m - l + 1
   n2 = r - m

   L = [None] * n1
   R = [None] * n2

   for i in range(n1):
      L[i] = list[l+i]

   for j in range(n2):
      R[j] = list[m+1+j]

   i = 0
   j = 0
   k = l

   while i<n1 and j<n2:
      if(L[i] <= R[j]):
         list[k] = L[i]
         i += 1
      else:
         list[k] = R[j]
         j += 1
      k += 1

   while i<n1:
      list[k] = L[i]
      i += 1
      k += 1

   while j<n2:
      list[k] = R[j]
      j += 1
      k += 1
   
def mergeSort(list,l,r):
   if(l<r):
      m = (l+(r-1))//2
      mergeSort(list,l,m)
      mergeSort(list,m+1,r)
      merge(list,l,m,r)
   return list


print(mergeSort([-3,6,1,0,9,-2,8,-4,7,-5],0,9)) 