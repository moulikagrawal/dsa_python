def longestCommonSubsequence(s1,s2,index1,index2,memory):
   if(len(s1) == index1 or len(s2) == index2):
      return 0
   if(s1[index1] == s2[index2]):
      return 1 + longestCommonSubsequence(s1,s2,index1+1,index2+1,memory)
   
   dictKey = (index1,index2)
   if(dictKey not in memory):
      op1 = longestCommonSubsequence(s1,s2,index1+1,index2,memory)
      op2 = longestCommonSubsequence(s1,s2,index1,index2+1,memory)
      memory[dictKey] =  max(op1,op2)
   return memory[dictKey]

print(longestCommonSubsequence("ABCDGH","AEDFHR",0,0,{}))