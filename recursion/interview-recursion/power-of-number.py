def powerOfNumber(n,power):
   if(power < 0):
      if(power == 0):
         return 1
      else:
         return 1/n * powerOfNumber(n,power+1)
   else:
      if(power == 0):
         return 1
      else:
         return n * powerOfNumber(n,power-1)

print(powerOfNumber(2.1,2.1))