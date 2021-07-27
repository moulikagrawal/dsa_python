def houseRobber(houses,currentHouse):
   if(currentHouse >= len(houses)):
      return 0
   stealHouse = houses[currentHouse] + houseRobber(houses,currentHouse+2)
   skipHouse = houseRobber(houses,currentHouse+1)
   return max(stealHouse,skipHouse)

print(houseRobber([6,7,1,30,8,2,4],0))