class Graph:
   def __init__(self,dict=None):
      if(dict):
         self.graphDict = dict
      else:
         self.graphDict = {}

   def addEdge(self,vertex,edge):
      self.graphDict[vertex].append(edge)

   def BFS(self,vertex):
      queue = [vertex]
      visited = [vertex]
      while queue:
         dequeuedVertex = queue.pop(0)
         print(dequeuedVertex,end=" ")
         for adjacentVertex in self.graphDict[dequeuedVertex]:
            if(adjacentVertex not in visited):
               visited.append(adjacentVertex)
               queue.append(adjacentVertex)

   def DFS(self,vertex):
      stack = [vertex]
      visited = [vertex]

      while stack:
         poppedVertex = stack.pop()
         print(poppedVertex,end=" ")
         for adjacentVertex in self.graphDict[poppedVertex]:
            if(adjacentVertex not in visited):
               visited.append(adjacentVertex)
               stack.append(adjacentVertex)

dict = {
   "6":["4"],
   "4":["5","3"],
   "3":["4","2"],
   "2":["3","5","1"],
   "5":["4","2","1"],
   "1":["5","2"]
}

graph = Graph(dict)
# graph.BFS("6")
graph.DFS("6")