def longestSubsequence(string,index1,index2,memory):
   if(len(string) == index1 or len(string) == index2):
      return 0
   
   if(string[index1] == string[index2] and index1 != index2):
      return 1 + longestSubsequence(string,index1+1,index2+1,memory)

   dictKey = (index1,index2)
   if(dictKey not in memory):
      op1 = longestSubsequence(string,index1+1,index2,memory)
      op2 = longestSubsequence(string,index1,index2+1,memory)
      memory[dictKey] = max(op1,op2)
   return memory[dictKey]

print(longestSubsequence("ATAKTKGGA",0,0,{}))