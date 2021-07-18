class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def BFS(self,source,destination):
      queue = []
      queue.append([source])
      while queue:
         path = queue.pop(0)
         node = path[-1]
         if(node == destination):
            return path
         for adjacentVertex in self.gdict.get(node,[]):
            newPath = list(path)
            newPath.append(adjacentVertex)
            queue.append(newPath)


dict = { "a" : ["b", "c"],
         "b" : ["d", "g"],
         "c" : ["d", "e"],
         "d" : ["f"],
         "e" : ["f"],
         "g" : ["f"]
       }

graph = Graph(dict)
print("-> ".join(graph.BFS("a", "d")))