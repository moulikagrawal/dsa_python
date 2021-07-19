class Graph:
   def __init__(self,vertices,edges,nodes):
      self.edges = edges
      self.nodes = nodes
      self.numberOfVertices = vertices
      self.MST = []

   def prims(self):
      visited = [False] * self.numberOfVertices
      visited[0] = True
      edgeNum = 0
      while edgeNum < self.numberOfVertices - 1:
         min = float("Inf")
         for i in range(self.numberOfVertices):
            if(visited[i]):
               for j in range(self.numberOfVertices):
                  if(not visited[j] and self.edges[i][j]):
                     if(min == float("Inf") or min > self.edges[i][j]):
                        min = self.edges[i][j]
                        s = i
                        d = j
         self.MST.append([self.nodes[s],self.nodes[d],self.edges[s][d]])
         visited[d] = True
         edgeNum += 1 

      for s,d,w in self.MST:
         print(s + " --- " + d + " => " + str(w))

edges = [[0, 10, 20, 0, 0],
		[10, 0, 30, 5, 0],
		[20, 30, 0, 15, 6],
		[0, 5, 15, 0, 8],
		[0, 0, 6, 8, 0]]
nodes = ["A","B","C","D","E"]
g = Graph(5, edges, nodes)
g.prims()
   