import math

def sumOfDigits(num):
   assert num >= 0 and int(num) == num , "Number is either not an integer or not a positive integer"
   if(num % 10 == 0):
      return num
   else:
      return num % 10 + sumOfDigits(math.floor(num / 10))

print(sumOfDigits(1245))