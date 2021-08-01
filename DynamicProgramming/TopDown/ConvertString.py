def convertString(s1,s2,index1,index2,memory):
   if(index1 == len(s1)):
      return len(s2) - index2
   if(index2 == len(s2)):
      return len(s1) - index1
   if(s1[index1] == s2[index2]):
      return convertString(s1,s2,index1+1,index2+1,memory)
   
   dictKey = (index1,index2)
   if(dictKey not in memory):
      delete = 1 + convertString(s1,s2,index1,index2+1,memory)
      insert = 1 + convertString(s1,s2,index1+1,index2,memory)
      replace = 1 + convertString(s1,s2,index1+1,index2+1,memory)
      memory[dictKey] = min(delete,insert,replace)
   return memory[dictKey]

print(convertString("table","tbres",0,0,{}))