def biggestNumber(arr):
   if(len(arr) == 1):
      return arr[0]
   else:
      big = arr[0]
      if(big < biggestNumber(arr[1:])):
         big = biggestNumber(arr[1:])
   return big

print(biggestNumber([1,4,2,8,7,58982,4]))

