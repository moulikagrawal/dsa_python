def convertString(s1,s2,index1,index2):
   if(index1 == len(s1)):
      return len(s2) - index2
   elif(index2 == len(s2)):
      return len(s1) - index1
   elif(s1[index1] == s2[index2]):
      return convertString(s1,s2,index1+1,index2+1)
   else:
      delete = 1 + convertString(s1,s2,index1,index2+1)
      insert = 1 + convertString(s1,s2,index1+1,index2)
      replace = 1 + convertString(s1,s2,index1+1,index2+1)
      return min(delete,insert,replace)
   
print(convertString("table","tbres",0,0))