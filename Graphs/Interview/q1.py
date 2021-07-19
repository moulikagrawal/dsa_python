# Given a directed graph and two nodes (S and E), 
# design an algorithm to find out whether there is a route from S to E.

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self, startNode, endNode):
         if(startNode == endNode):
            return True
         visited = [startNode]
         queue = [startNode]
         while queue:
            node = queue.pop(0)
            for i in self.gdict[node]:
               if(i == endNode):
                  return True
               if(i not in visited):
                  visited.append(i)
                  queue.append(i)
         return False

customDict = {
   "a" : ["c","d","b"],
   "b" : ["j"],
   "c" : ["g"],
   "d" : [],
   "e" : ["f","a"],
   "f" : ["i"],
   "g" : ["d","h"],
   "h" : [],
   "i" : [],
   "j" : []
}

g = Graph(customDict)
print(g.checkRoute("a","a"))