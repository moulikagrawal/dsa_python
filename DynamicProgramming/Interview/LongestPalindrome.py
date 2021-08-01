def longestPalindrome(s1,m,T):
   for i in range(1,m+1):
      for j in range(m-1,-1,-1):
         if(s1[i-1] == s1[j-1]):
            T[i][j] = T[i-1][j+1] + 1
         else:
            T[i][j] = max(T[i-1][j],T[i][j+1])
   return T[m][0]

s1="BBABCBCAB"
m = len(s1)
T = [[1 for x in range(m+1)] for x in range(m+1)]

print(longestPalindrome(s1,m,T))
# for i in range(len(T)):
#    for j in range(len(T)):
#       print(T[i][j],end=" ") 
#    print("\n")
