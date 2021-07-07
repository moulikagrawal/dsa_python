import queueList

class Tree:
   def __init__(self,data=None):
      self.data = data
      self.leftChild = None
      self.rightChild = None

   def searchTree(self,rootNode,value):
      if(not rootNode):
         return
      treeQueue = queueList.Queue()
      treeQueue.enqueue(rootNode)
      while(not treeQueue.isEmpty()):
         root = treeQueue.dequeue()
         if(root.value.data == value):
            return "Element is found"
         if(root.value.leftChild is not None):
              treeQueue.enqueue(root.value.leftChild) 
         if(root.value.rightChild is not None):
              treeQueue.enqueue(root.value.rightChild) 
      return "Element cannot be found"

def createTree():
   value = input("Enter None for no data => ")
   if(value == "None"):
      return None
   node = Tree()
   node.data = value

   print("\nEnter value for leftchild of " + node.data)
   node.leftChild = createTree()

   print("\nEnter value for rightchild of " + node.data)
   node.rightChild = createTree()

   return node

def preOrder(rootNode):
   if(not rootNode):
      return
   print(rootNode.data," ",end="")
   preOrder(rootNode.leftChild)
   preOrder(rootNode.rightChild)

def inOrder(rootNode):
   if(not rootNode):
      return
   inOrder(rootNode.leftChild)
   print(rootNode.data," ",end="")
   inOrder(rootNode.rightChild)
   
def postOrder(rootNode):
   if(not rootNode):
      return
   postOrder(rootNode.leftChild)
   postOrder(rootNode.rightChild)
   print(rootNode.data," ",end="")

def levelOrder(rootNode):
   if(not rootNode):
      return
   treeQueue = queueList.Queue()
   treeQueue.enqueue(rootNode)
   while(not treeQueue.isEmpty()):
      root = treeQueue.dequeue()
      print(root.value.data," ",end="")

      if(root.value.leftChild is not None):
           treeQueue.enqueue(root.value.leftChild) 
      if(root.value.rightChild is not None):
           treeQueue.enqueue(root.value.rightChild) 

def insertTree(node,rootNode):
   if(not rootNode):
      rootNode = node
      return "RootNode Created"
      
   treeQueue = queueList.Queue()
   treeQueue.enqueue(rootNode)
   while(not treeQueue.isEmpty()):
      root = treeQueue.dequeue()

      if(root.value.leftChild is not None):
         treeQueue.enqueue(root.value.leftChild)
      else:
         root.value.leftChild = node
         return "Element Added as leftChild of " + root.value.data

      if(root.value.rightChild is not None):
         treeQueue.enqueue(root.value.rightChild)
      else:
         root.value.rightChild = node
         return "Element Added as rightChild of " + root.value.data

def deepestNode(rootNode):
   if(not rootNode):
      return
   treeQueue = queueList.Queue()
   treeQueue.enqueue(rootNode)
   while(not treeQueue.isEmpty()):
      root = treeQueue.dequeue()

      if(root.value.leftChild is not None):
           treeQueue.enqueue(root.value.leftChild) 
      if(root.value.rightChild is not None):
           treeQueue.enqueue(root.value.rightChild)

   return root.value

def deleteDeepestNode(rootNode):
   if(not rootNode):
      return
   dNode = deepestNode(rootNode)
   
   treeQueue = queueList.Queue()
   treeQueue.enqueue(rootNode)

   while(not treeQueue.isEmpty()):
      root = treeQueue.dequeue()
      if(root.value is dNode):
         root.value = None
         return
      if(root.value.leftChild):
         if(root.value.leftChild is dNode):
            root.value.leftChild = None
            return
         treeQueue.enqueue(root.value.leftChild)
      if(root.value.rightChild):
         if(root.value.rightChild is dNode):
            root.value.rightChild = None
            return
         treeQueue.enqueue(root.value.rightChild)
      
def deleteNodeTree(value,rootNode):
   if(not rootNode):
      return "Tree is Empty"
   
   treeQueue = queueList.Queue()
   treeQueue.enqueue(rootNode)
   dNode = deepestNode(rootNode)

   while(not treeQueue.isEmpty()):
      root = treeQueue.dequeue()
      if(root.value.data == value):
         root.value.data = dNode.data
         deleteDeepestNode(rootNode)
         return
      
      if(root.value.leftChild is not None):
           treeQueue.enqueue(root.value.leftChild) 
      if(root.value.rightChild is not None):
           treeQueue.enqueue(root.value.rightChild)

def deleteTree(rootNode):
   if(not rootNode):
      return
   
   rootNode.data = None
   rootNode.leftChild = None
   rootNode.rightChild = None
   
rootNode = createTree()

# rootNode.preOrder(rootNode)
# rootNode.inOrder(rootNode)
# rootNode.postOrder(rootNode)
# rootNode.levelOrder(rootNode)

# found = rootNode.searchTree(rootNode,"2")
# print("\n",found)

# node = Tree(3)
# print(insertTree(node,rootNode))
# levelOrder(rootNode)

# print(deepestNode(rootNode).data)

# levelOrder(rootNode)
# deleteDeepestNode(rootNode)
# print("\n")
# levelOrder(rootNode)

# levelOrder(rootNode)
# deleteNodeTree("2",rootNode)
# print("\n")
# levelOrder(rootNode)

levelOrder(rootNode)
deleteTree(rootNode)
print("\n")
levelOrder(rootNode)