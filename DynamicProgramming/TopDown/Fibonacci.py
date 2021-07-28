def fibonacci(n,memory):
   if(n == 1):
      return 0
   if(n == 2):
      return 1
   if(n not in memory):
      memory[n] = fibonacci(n-1,memory) + fibonacci(n-2,memory)
   return memory[n]

dict = {}
print(fibonacci(6,dict))