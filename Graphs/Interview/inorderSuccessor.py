class Node: 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

def insert(node, data):
   if node is None:
       return Node(data)
   else:
       if data <= node.data:
           temp = insert(node.left, data)
           node.left = temp
           temp.parent = node
       else:
           temp = insert(node.right, data)
           node.right = temp
           temp.parent = node      
       return node

def inOrderSuccessor(root, n):
   if(not root):
      return
   if(root.data == n):
      if(root.right is not None):
         inOrderSuccessor(root.right)
      else:
         
