from collections import defaultdict

class Graph:
   def __init__(self,numberOfVertices):
      self.graph = defaultdict(list)
      self.numberOfVertices = numberOfVertices

   def addEdge(self,vertex,edge):
      self.graph[vertex].append(edge)

   def topologicalSortUtil(self,vertex,visited,stack):
      visited.append(vertex)
      for adjacentVertex in self.graph[vertex]:
         if(adjacentVertex not in visited):
            self.topologicalSortUtil(adjacentVertex,visited,stack)
      stack.append(vertex)
      
   def topologicalSort(self):
      visited = []
      stack = []

      for vertex in list(self.graph):
         if(vertex not in visited):
            self.topologicalSortUtil(vertex,visited,stack)

      print(stack[::-1])

graph = Graph(8)
graph.addEdge("A", "C")
graph.addEdge("C", "E")
graph.addEdge("E", "H")
graph.addEdge("E", "F")
graph.addEdge("F", "G")
graph.addEdge("B", "D")
graph.addEdge("B", "C")
graph.addEdge("D", "F")
graph.topologicalSort()