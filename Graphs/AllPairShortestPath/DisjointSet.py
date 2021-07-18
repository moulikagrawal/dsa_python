class DisjointSet:
   def __init__(self,vertices):
      self.vertices = vertices
      self.parent = {}
      self.rank = {}
      for vertice in vertices:
         self.parent[vertice] = vertice
         self.rank[vertice] = 0

   def findSet(self,item):
      if(self.parent[item] == item):
         return item
      return self.findSet(self.parent[item])

   def union(self,x,y):
      xroot = self.findSet(x)
      yroot = self.findSet(y)

      if(self.rank[xroot] < self.rank[yroot]):
         self.parent[xroot] = yroot
      elif(self.rank[xroot] > self.rank[yroot]):
         self.parent[yroot] = xroot
      else:
         self.parent[yroot] = xroot
         self.rank[xroot] += 1

vertices = ["A","B","C","D","E"]
disjointSet = DisjointSet(vertices)
disjointSet.union("B","C") 
disjointSet.union("B","E")
print(disjointSet.findSet("E")) 