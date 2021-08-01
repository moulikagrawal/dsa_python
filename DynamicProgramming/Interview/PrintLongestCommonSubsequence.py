def lookupTable(s1,s2,m,n,T):
   for i in range(1,m+1):
      for j in range(1,n+1):
         if(s1[i-1] == s2[j-1]):
            T[i][j] = T[i-1][j-1] + 1
         else:
            T[i][j] = max(T[i-1][j],T[i][j-1])

def LCS(s1,s2,m,n,T):
   if(m == 0 or n == 0):
      return str()
   if(s1[m-1] == s2[n-1]):
      return LCS(s1,s2,m-1,n-1,T) + s1[m-1]
   if(T[m-1][n] >= T[m][n-1]):
      return LCS(s1,s2,m-1,n,T)
   return LCS(s1,s2,m,n-1,T)
   

s1 = "ABCBDAB"
s2 = "BDCABA"
m = len(s1)
n = len(s2)
T =[[0 for x in range(n+1)] for x in range(m+1)]

lookupTable(s1,s2,m,n,T)
subsequence = LCS(s1,s2,m,n,T)
print(subsequence)