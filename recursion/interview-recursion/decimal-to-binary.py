def decimalToBinary(num):
   if(num == 1):
      return "1"
   else:
      return str(num%2) + decimalToBinary(int(num/2)) 

print(decimalToBinary(128)[::-1])

# def decimalToBinary(num):
#    if(num == 1):
#       return 1
#    else:
#       return num%2 + 10 * decimalToBinary(int(num/2)) 