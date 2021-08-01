def subsetSum(list,sum,index):
   if(sum == 0):
      return True
   elif(index == 0):
      return False
   elif(list[index-1] > sum):
      return subsetSum(list,sum,index-1)
   else:
      op1 = subsetSum(list,sum-list[index-1],index-1)
      op2 = subsetSum(list,sum,index-1)
      return op1 or op2

list = [3,34,4,12,6,5]
print(subsetSum(list,30,len(list)))