def houseRobber(houses):
   table = [0] * len(houses)+2
   for i in range(len(houses)-1,-1,-1):
      table[i] = max(houses[i]+table[i+2],table[i+1])
   return table[0]

print(houseRobber([6,7,1,30,8,2,4]))