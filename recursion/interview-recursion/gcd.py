def gcd(num1,num2):
   if(num1 < 0):
      num1 *= -1
   if(num2 < 0):
      num2 *= -1

   if(num1 % num2 != 0):
      return gcd(num2,num1 % num2)
   else:
      return num2

print(gcd(12,-1))