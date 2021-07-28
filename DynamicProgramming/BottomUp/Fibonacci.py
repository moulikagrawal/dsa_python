def fibonacci(n):
   table =  [0,1]
   for i in range(2,n+1):
      table.append(table[i-1]+table[i-2])
   return table[n-1]

print(fibonacci(6))