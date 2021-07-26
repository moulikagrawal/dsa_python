def coinChange(amount,change):
   dict = {}
   while(amount != 0):
      maximum = max(change)
      if(maximum > amount):
         change.remove(maximum)
      else:
         if(maximum in dict):
            dict[maximum] += 1
         else:
            dict[maximum] = 1
         amount -= maximum
   return dict

print(coinChange(2035,{10,1,100,20,2,1000,5}))
   