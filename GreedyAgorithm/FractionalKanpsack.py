def fractionalKnapsack(list,limit):
   density = []
   for weight,value in list:
      density.append([weight,value,value/weight])
   density = sorted(density,key=lambda d:d[2],reverse=True)
   
   maxValue = 0
   i = 0
   while(limit != 0 or i != len(density)):
      if(limit < density[i][0]):
         maxValue += (limit/density[i][0])*density[i][1]
         limit -= (limit/density[i][0])*density[i][0]
      else:
         maxValue += density[i][1]
         limit -= density[i][0]
      i += 1
   return maxValue

print(fractionalKnapsack([(20,100),(10,60),(30,120)],50))