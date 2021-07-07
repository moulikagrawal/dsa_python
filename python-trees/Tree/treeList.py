class BinaryTree:
   def __init__(self,size):
      self.list = size * [None]
      self.lastUsedIndex = 0
      self.size = size

   def insertTree(self,value):
      if(self.lastUsedIndex + 1 == self.size):
         return "Tree is full"   
         
      self.list[self.lastUsedIndex + 1] = value
      self.lastUsedIndex += 1
      return "Element " + str(value) + " inserted in the Tree"

   def searchTree(self,value):
      for i in range(1,self.lastUsedIndex+1):
         if(self.list[i] == value):
            return "Element " + str(value) + "  is found"
      return "Element " + str(value) + " cannot be found"

   def preOrder(self,index):
      if(index > self.lastUsedIndex):
         return
      print(self.list[index],end=" ")
      self.preOrder(2*index)
      self.preOrder(2*index+1)

   def inOrder(self,index):
      if(index > self.lastUsedIndex):
         return
      self.inOrder(2*index)
      print(self.list[index],end=" ")
      self.inOrder(2*index+1)

   def postOrder(self,index):
      if(index > self.lastUsedIndex):
         return
      self.postOrder(2*index)
      self.postOrder(2*index+1)
      print(self.list[index],end=" ")

   def levelOrder(self):
      for i in range(1, self.lastUsedIndex+1):
         print(self.list[i],end=" ")

   def deleteNode(self,value):
      if(self.lastUsedIndex == 0):
         return
      for i in range(1,self.lastUsedIndex+1):
         if(self.list[i] == value):
            self.list[i] = self.list[self.lastUsedIndex]
            self.list[self.lastUsedIndex] = None
            self.lastUsedIndex -= 1
      
   def deleteTree(self):
      self.list = None
      self.lastUsedIndex = 0

tree = BinaryTree(10)
tree.insertTree(1)
tree.insertTree(2)
tree.insertTree(3)
tree.insertTree(4)
tree.insertTree(5)

# print(tree.searchTree(3))
# print(tree.searchTree(10))

# tree.preOrder(1)
# print("\n")
# tree.inOrder(1)
# print("\n")
# tree.postOrder(1)
# print("\n")
# tree.levelOrder()

# tree.levelOrder()
# print("\n")
# tree.deleteNode(2)
# tree.levelOrder()

tree.levelOrder()
print("\n")
tree.deleteTree()
tree.levelOrder()