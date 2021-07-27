def numberOfPaths(list,i,j,cost):
   if(cost < 0):
      return 0
   elif(i == len(list)-1 and j == len(list)-1):
      if(list[i][j] - cost == 0):
         return 1
      return 0
   elif(i == len(list)-1):
      return numberOfPaths(list,i,j+1,cost-list[i][j])
   elif(j == len(list)-1):
      return numberOfPaths(list,i+1,j,cost-list[i][j])
   else:
      op1 = numberOfPaths(list,i+1,j,cost-list[i][j])
      op2 = numberOfPaths(list,i,j+1,cost-list[i][j])
      return op1+op2

list = [
   [4,7,1,6],
   [5,7,3,9],
   [3,2,1,2],
   [7,1,6,3],
]
print(numberOfPaths(list,0,0,25))