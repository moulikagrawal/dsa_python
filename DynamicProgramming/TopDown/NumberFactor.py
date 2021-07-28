def numberFactor(n,memory):
   if(n < 0):
      return 0
   if(n == 0 or n == 1 or n == 2):
      return 1
   if(n not in memory):
      memory[n] = numberFactor(n-1,memory) + numberFactor(n-3,memory) + numberFactor(n-4,memory)
   return memory[n]

print(numberFactor(5,{}))