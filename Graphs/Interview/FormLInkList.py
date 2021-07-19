class LinkedList:
   def __init__(self,value=None):
      self.val = value
      self.next = None
   
   def add(self,value):
      if(self.next == None):
         self.next = LinkedList(value)
      else:
         self.next.add(value)

   def __str__(self):
      return "({val})".format(val = self.val) + str(self.next)

class BinaryTree:
   def __init__(self,data):
      self.data = data
      self.left = None
      self.right = None

def depth(tree):
   if(not tree):
      return 0
   if(tree.left == None and tree.right == None):
      return 1
   else:
      depthLeft = 1 + depth(tree.left)
      depthRight = 1 + depth(tree.right)
      if(depthRight > depthLeft):
         return depthRight
      return depthLeft

def treeToLinkedList(tree, dict={}, d=None):
   # if(not tree):
   #    return
   if(not d):
      d = depth(tree)
   if(dict.get(d) == None):
      dict[d] = LinkedList(tree.data)
   else:
      dict[d].add(tree.data)
      if(d == 1):
         return dict
   if(tree.left):
      treeToLinkedList(tree.left,dict,d-1)
   if(tree.right):
      treeToLinkedList(tree.right,dict,d-1)
   return dict

tree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)

tree.left = two
tree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

dict = treeToLinkedList(tree)
for i,j in dict.items():
   print("{0} {1}".format(i,j))