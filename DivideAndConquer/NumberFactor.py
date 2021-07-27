def numberFactor(n):
   if(n < 0):
      return 0
   if(n == 0 or n == 1 or n == 2):
      return 1
   return numberFactor(n-1) + numberFactor(n-3) + numberFactor(n-4)

print(numberFactor(4))