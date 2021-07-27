def minimumCost(list,i,j):
   if(i == len(list)-1 and j == len(list)-1):
      return list[i][j] 

   if(i == len(list)-1):
      if(j != len(list)-1):
         return list[i][j] + minimumCost(list,i,j+1)

   if(j == len(list)-1):
      if(i != len(list)-1):
         return list[i][j] + minimumCost(list,i+1,j)
      
   chosen1 = list[i][j] + minimumCost(list,i+1,j)
   chosen2 = list[i][j] + minimumCost(list,i,j+1)

   return min(chosen1,chosen2)

list = [
   [4,7,8,6,4],
   [6,7,3,9,2],
   [3,8,1,2,4],
   [7,1,7,3,7],
   [2,9,8,9,3]
]
print(minimumCost(list,0,0))