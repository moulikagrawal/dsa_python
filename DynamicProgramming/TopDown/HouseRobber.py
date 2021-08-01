def houseRobber(houses,currentHouse,memory):
   if(currentHouse >= len(houses)):
      return 0
   if(currentHouse not in memory):
      stolenHouse = houses[currentHouse] + houseRobber(houses,currentHouse+2,memory)
      skippedHouse = houseRobber(houses,currentHouse+1,memory)
      memory[currentHouse] = max(stolenHouse,skippedHouse)
      print(memory)
   return memory[currentHouse]

print(houseRobber([6,7,1,30,8,2,4],0,{}))