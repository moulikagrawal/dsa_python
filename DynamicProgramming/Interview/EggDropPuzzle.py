import sys

def eggDrop(floors,eggs):
   # if(eggs == 1):
   #    return floors
   # if(floors == 1 or floors == 0):
   #    return 1
   
   # min = sys.maxsize
   # for block in range(1,floors+1):
   #    op1 = eggDrop(block-1,eggs-1)
   #    op2 = eggDrop(floors-block,eggs)
   #    result = max(op1,op2)
   #    if(result < min):
   #       min = result + 1
   # return min

   T = [[0 for x in range(eggs+1)] for x in range(floors+1)]
   for i in range(1,eggs+1):
      T[0][i] = 0
      T[1][i] = 1
   for i in range(1,floors+1):
      T[i][0] = i
   
   for i in range(1,floors+1):
      for j in range(1,eggs+1):
         T[i][j] = sys.maxsize
         for x in range(i+1):
            result = 1 + max(T[x-1][j-1],T[i-x][j])
            if(result < T[i][j]):
               T[i][j] = result
   
   for i in range(floors+1):
      for j in range(eggs+1):
         print(T[i][j],end=" ")
      print()
   return T[floors][eggs-1]
   
print(eggDrop(100,2))