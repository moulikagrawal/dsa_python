class Graph:
   def __init__(self,vertices):
      self.numberOfVertices = vertices
      self.edges = []
      self.nodes = []

   def addNode(self,value):
      self.nodes.append(value)

   def addEdge(self,source,destination,weight):
      self.edges.append([source,destination,weight])

   def bellmanFord(self,initialNode,finalNode):
      dist = {}
      parent = {}
      for i in self.nodes:
         dist[i] = float("Inf")
      dist[initialNode] = 0

      for i in range(self.numberOfVertices - 1):
         for source,destination,weight in self.edges:
            if(dist[source] != float("Inf") and 
                  dist[destination] > weight + dist[source]):
               dist[destination] = weight + dist[source]
               parent[destination] = source
      
      for source,destination,weight in self.edges:
         if(dist[source] != float("Inf") and 
                  dist[destination] > weight + dist[source]):
            print("Negative cycle is present")
            return

      def findPath(path,finalNode,initialNode,finalPath):
         node = path[finalNode][0]
         finalPath.append(node)
         if(node == initialNode):
            return finalPath
         findPath(path,node,initialNode,finalPath)
         return finalPath

      finalPath = []
      finalPath = findPath(parent,finalNode,initialNode,finalPath)
      finalPath.insert(0,finalNode)
      ff = "-> ".join(finalPath[::-1])

      print(dist)
      print(ff)

graph = Graph(5)
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
graph.addNode("E")
graph.addEdge("A", "C", 6)
graph.addEdge("A", "D", 6)
graph.addEdge("B", "A", 3)
graph.addEdge("C", "D", 1)
graph.addEdge("D", "C", 2)
graph.addEdge("D", "B", 1)
graph.addEdge("E", "B", 4)
graph.addEdge("E", "D", 2)
graph.bellmanFord("E","A")