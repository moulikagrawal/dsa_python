import queueList

class AVLNode:
   def __init__(self,data=None):
      self.data = data
      self.leftChild = None
      self.rightChild = None
      self.height = 1

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

def searchTree(rootNode,nodeValue):
   if(rootNode.data == nodeValue):
      print("Value is found")
   elif(nodeValue < rootNode.data):
      if(rootNode.leftChild.data == nodeValue):
         print("Value is found")
      else:
         searchTree(rootNode.leftChild,nodeValue)
   elif(nodeValue > rootNode.data):
      if(rootNode.rightChild.data == nodeValue):
         print("Value is found")
      else:
         searchTree(rootNode.rightChild,nodeValue)

def getHeight(rootNode):
   if(not rootNode):
      return 0
   return rootNode.height

def rotateLeft(disbalancedNode):
   newRoot = disbalancedNode.rightChild
   disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
   newRoot.leftChild = disbalancedNode
   disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
   newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
   return newRoot

def rotateRight(disbalancedNode):
   newRoot = disbalancedNode.leftChild
   disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
   newRoot.rightChild = disbalancedNode
   disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
   newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
   return newRoot

def getBalance(rootNode):
   if(not rootNode):
      return 0 
   return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode,nodeValue):
   if(not rootNode):
      return AVLNode(nodeValue)
   elif(nodeValue <= rootNode.data):
      rootNode.leftChild = insertNode(rootNode.leftChild,nodeValue)
   else:
      rootNode.rightChild = insertNode(rootNode.rightChild,nodeValue)

   rootNode.height = 1 + max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
   balance = getBalance(rootNode)
   if(balance > 1 and nodeValue < rootNode.leftChild.data):
      return rotateRight(rootNode)
   if(balance > 1 and nodeValue > rootNode.leftChild.data):
      rootNode.leftChild = rotateLeft(rootNode.leftChild)
      return rotateRight(rootNode)
   if(balance < -1 and nodeValue > rootNode.rightChild.data):
      return rotateLeft(rootNode)
   if(balance < -1 and nodeValue < rootNode.rightChild.data):
      rootNode.rightChild = rotateRight(rootNode.rightChild)
      return rotateLeft(rootNode)

   return rootNode

def getMinimumNode(rootNode):
   if(not rootNode.leftChild):
      return rootNode

   return getMinimumNode(rootNode.leftChild)

def deleteNode(rootNode,nodeValue):
   if(not rootNode):
      return rootNode
   elif(nodeValue < rootNode.data):
      rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
   elif(nodeValue > rootNode.data):
      rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)
   else:
      if(rootNode.leftChild is None):
         temp = rootNode.rightChild
         rootNode = None
         return temp
      elif(rootNode.rightChild is None):
         temp = rootNode.leftChild
         rootNode = None
         return temp
      else:
         temp = getMinimumNode(rootNode.rightChild)
         rootNode.data = temp.data
         rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)
      
   rootNode.height = 1 + max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
   balance = getBalance(rootNode)
   if(balance > 1 and getBalance(rootNode.leftChild) >= 0):
      return rotateRight(rootNode)
   if(balance > 1 and getBalance(rootNode.leftChild) < 0):
      rootNode.leftChild = rotateLeft(rootNode.leftChild)
      return rotateRight(rootNode)
   if(balance < -1 and getBalance(rootNode.rightChild) <= 0):
      return rotateLeft(rootNode)
   if(balance < -1 and getBalance(rootNode.rightChild) > 0):
      rootNode.rightChild = rotateRight(rootNode.rightChild)
      return rotateLeft(rootNode)
     
   return rootNode

def deleteAVL(rootNode):
   rootNode.data = None
   rootNode.leftChild = None
   rootNode.rightChild = None
   return "AVL is successfully deleted"

avl = AVLNode(30)
avl = insertNode(avl,25)
avl = insertNode(avl,35)
avl = insertNode(avl,20)
avl = insertNode(avl,15)
avl = insertNode(avl,5)
avl = insertNode(avl,10)
avl = insertNode(avl,50)
avl = insertNode(avl,60)
avl = insertNode(avl,70)
avl = insertNode(avl,65)
# levelOrderTraversal(avl)
# print("\n")
# avl = deleteNode(avl,5)
# avl = deleteNode(avl,15)
# levelOrderTraversal(avl)

print(deleteAVL(avl))
levelOrderTraversal(avl)