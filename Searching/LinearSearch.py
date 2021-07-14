def linearSearch(list,value):
   for i in range(len(list)):
      if(list[i] == value):
         return "Value is found at position " + str(i+1)
   return "Value cannot be found"

print(linearSearch([6,1,9,4,3,0,2,8],0))