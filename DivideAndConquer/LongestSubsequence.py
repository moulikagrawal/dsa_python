def longestSubsequence(s1,s2,index1,index2):
   if(len(s1) == index1 or len(s2) == index2):
      return 0
   if(s1[index1] == s2[index2]):
      return 1 + longestSubsequence(s1,s2,index1+1,index2+1)

   skipS1 = longestSubsequence(s1,s2,index1+1,index2)
   skipS2 = longestSubsequence(s1,s2,index1,index2+1) 
   return max(skipS1,skipS2)

print(longestSubsequence("elephant","erepat",0,0))