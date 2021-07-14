def binarySearch1(sortedList,value,left,right):
   if(right >= left):
      mid = (left + right)//2
      if(sortedList[mid] < value):
         left = mid + 1
         return binarySearch1(sortedList,value,left,right)
      elif(sortedList[mid] > value):
         right = mid - 1
         return binarySearch1(sortedList,value,left,right)
      else:
         return "Value is found at postion " + str(mid+1)
   else:
      return "Value cannot be found"

def binarySearch2(sortedList,value):
   left = 0
   right = len(sortedList)-1

   while(right >= left):
      mid = (left+right)//2
      if(sortedList[mid] > value):
         right = mid - 1
      elif(sortedList[mid] < value):
         left = mid + 1
      else:
         return "Value is found at postion " + str(mid+1)

   return "Value cannot be found"

sortedList = [1,2,3,4,5,6,7,8,9]
print(binarySearch1(sortedList,92,0,len(sortedList)-1))
print(binarySearch2(sortedList,7))