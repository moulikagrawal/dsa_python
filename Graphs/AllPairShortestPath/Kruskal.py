import DisjointSet

class Graph:
   def __init__(self,vertices):
      self.numberOfVertices = vertices
      self.nodes = []
      self.edges = []
      self.MST = []

   def addEdge(self,source,destination,weight):
      self.edges.append([source,destination,weight])

   def addNode(self,vertex):
      self.nodes.append(vertex)

   def kruskal(self):
      i,j = 0,0
      dst = DisjointSet.DisjointSet(self.nodes)
      self.edges = sorted(self.edges, key= lambda item:item[2])
      while j < self.numberOfVertices-1:
         edge_src, edge_dest, edge_wt = self.edges[i]
         i += 1
         x = dst.findSet(edge_src)
         y = dst.findSet(edge_dest)
         if(x != y):
            j += 1
            self.MST.append([edge_src,edge_dest,edge_wt])
            dst.union(x,y)

      for s,d,w in self.MST:
         print(s + " --- " + d + " => " + str(w))

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskal()