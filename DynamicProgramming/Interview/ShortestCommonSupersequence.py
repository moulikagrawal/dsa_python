def shortestCommonSupersequence(s1,s2,m,n,T):
   for i in range(1,m+1):
      for j in range(1,n+1):
         if(s1[i-1] == s2[j-1]):
            T[i][j] = T[i-1][j-1] - 1
         else:
            T[i][j] = min(T[i-1][j],T[i][j-1])

   return T[m][n]

s1="ABCBDAB"
s2="BDCABA"
m = len(s1)
n = len(s2)
T = [[m+n for x in range(n+1)] for x in range(m+1)]
print(shortestCommonSupersequence(s1,s2,m,n,T))