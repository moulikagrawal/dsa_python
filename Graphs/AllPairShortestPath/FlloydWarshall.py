class Graph:
   def __init__(self,vertices,distances):
      self.numberOfVertices = vertices
      self.distances = distances

   def flloydWarshall(self):
      distances = self.distances
      for i in range(self.numberOfVertices):
         for j in range(self.numberOfVertices):
            for k in range(self.numberOfVertices):
               if(distances[j][k] == float("Inf") or
                  distances[j][k] > distances[j][i] + distances[i][k]):
                  distances[j][k] = distances[j][i] + distances[i][k]   

      for i in range(self.numberOfVertices):
         for j in range(self.numberOfVertices):
            print(distances[i][j],end=" ")
         print(" ")

distances = [
      [0, 8, float("Inf"), 1],
      [float("Inf"), 0, 1, float("Inf")],
      [4, float("Inf"), 0, float("Inf")],
      [float("Inf"), 2, 9, 0]
    ]

graph = Graph(4,distances)
graph.flloydWarshall()
