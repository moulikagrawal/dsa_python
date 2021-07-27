def longestPalindromicSubsequence(s,startIndex,lastIndex):
   if(startIndex > lastIndex):
      return 0
   if(startIndex == lastIndex):
      return 1
   if(s[startIndex] == s[lastIndex]):
      return 2 + longestPalindromicSubsequence(s,startIndex+1,lastIndex-1) 

   op1 = longestPalindromicSubsequence(s,startIndex+1,lastIndex)
   op2 = longestPalindromicSubsequence(s,startIndex,lastIndex-1)
   return max(op1,op2)

s = "elrmenmet"
print(longestPalindromicSubsequence(s,0,len(s)-1))