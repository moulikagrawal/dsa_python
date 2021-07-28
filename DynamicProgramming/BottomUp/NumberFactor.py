def numberFactor(n):
   if(n == 0):
      return 0
   table = [1,1,1,2]
   for i in range(4,n+1):
      table.append(table[i-1] + table[i-3] + table[i-4])
   return table[n]

print(numberFactor(0))