import queueList

class BST:
   def __init__(self,data):
      self.data = data
      self.leftChild = None
      self.rightChild = None

def insertTree(rootNode,nodeValue):
   if(rootNode.data == None):
      rootNode.data = nodeValue
      return str(nodeValue) + " has been inserted to rootNode of BST"
   
   elif(nodeValue <= rootNode.data):
      if(rootNode.leftChild is not None):
         insertTree(rootNode.leftChild,nodeValue)
      else:
         rootNode.leftChild = BST(nodeValue)
   else:
      if(rootNode.rightChild is not None):
         insertTree(rootNode.rightChild,nodeValue)
      else:
         rootNode.rightChild = BST(nodeValue)
   
   return str(nodeValue) + " has been inserted to BST"

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data,end=" ")
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data,end=" ")

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data,end=" ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def levelOrderTraversal(rootNode):
   if(not rootNode):
      return
   
   treeQueue = queueList.Queue()
   treeQueue.enqueue(rootNode)

   while(not treeQueue.isEmpty()):
      root = treeQueue.dequeue()
      print(root.value.data,end=" ")

      if(root.value.leftChild is not None):
         treeQueue.enqueue(root.value.leftChild)
      if(root.value.rightChild is not None):
         treeQueue.enqueue(root.value.rightChild)

def searchTree(rootNode,value):
   if(not rootNode):
      return

   if(rootNode.data == value):
      print("Element found")
      return

   if(value < rootNode.data):
      if(rootNode.leftChild):
         searchTree(rootNode.leftChild,value)
   else:
      if(rootNode.rightChild):
         searchTree(rootNode.rightChild,value)

def minimumNode(rootNode):
   currentNode = rootNode
   while(currentNode.leftChild is not None):
      currentNode = currentNode.leftChild
   
   return currentNode

def deleteNode(rootNode,nodeValue):
   if(rootNode is None):
      return rootNode
   
   if(nodeValue < rootNode.data):
      rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
   elif(nodeValue > rootNode.data):
      rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)
   else:
      if(rootNode.leftChild is None):
         temp = rootNode.rightChild
         rootNode = None
         return temp
      
      if(rootNode.rightChild is None):
         temp = rootNode.leftChild
         rootNode = None
         return temp
      
      temp = minimumNode(rootNode.rightChild)
      rootNode.data = temp.data
      rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)
   return rootNode

def deleteTree(rootNode):
   rootNode.leftChild = None
   rootNode.rightChild = None
   rootNode.data = None

tree = BST(None)

insertTree(tree, 70)
insertTree(tree,50)
insertTree(tree,90)
insertTree(tree, 30)
insertTree(tree,60)
insertTree(tree,80)
insertTree(tree,100)
insertTree(tree,20)
insertTree(tree,40)

# inOrderTraversal(tree)
# print("\n")
# preOrderTraversal(tree)
# print("\n")
# postOrderTraversal(tree)
# print("\n")
# levelOrderTraversal(tree)

# searchTree(tree,40)

# levelOrderTraversal(tree)
# deleteNode(tree,30)
# print("\n")
# levelOrderTraversal(tree)

levelOrderTraversal(tree)
deleteTree(tree)
print("\n")
levelOrderTraversal(tree)
