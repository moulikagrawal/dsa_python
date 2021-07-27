def zeroKnapsack(fruits,currentIndex,capacity):
   if(currentIndex >= len(fruits) or capacity <= 0):
      return 0
   elif(fruits[currentIndex][1] <= capacity):
      op1 = fruits[currentIndex][2] + zeroKnapsack(fruits,currentIndex+1,capacity-fruits[currentIndex][1])
      op2 = zeroKnapsack(fruits,currentIndex+1,capacity)
      return max(op1,op2)
   else:
      return 0

fruits = [
            ["Mango",3,31],
            ["Apple",1,26],
            ["Orange",2,17],
            ["Banana",5,72]
         ]
print(zeroKnapsack(fruits,0,7))