def zeroKnapsack(items,currentItem,capacity,memory):
   if(currentItem >= len(items) or capacity <= 0):
      return 0
   elif(items[currentItem][1] <= capacity):
      dictKey = (currentItem,capacity)
      if(dictKey not in memory):
         op1 = items[currentItem][2] + zeroKnapsack(items,currentItem+1,capacity-items[currentItem][1],memory)
         op2 = zeroKnapsack(items,currentItem+1,capacity,memory)
         memory[dictKey] = max(op1,op2)
      return memory[dictKey]
   return 0

items = [
            ["Mango",3,31],
            ["Apple",1,26],
            ["Orange",2,17],
            ["Banana",5,72]
         ]
print(zeroKnapsack(items,0,7,{}))