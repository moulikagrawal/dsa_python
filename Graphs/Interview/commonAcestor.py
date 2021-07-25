class Node:
   def __init__(self, value, left=None, right=None):
      self.value = value
      self.right = right
      self.left = left

def findNode(root,n):
   if(not root.left or not root.right):
      return False
   if(root.left.value == n or root.right.value == n):
      return True
   return findNode(root.left,n) or findNode(root.right,n)

def findFirstCommonAncestor(n1, n2, root,value=None):
   if(not root):
      return value
   foundN1 = findNode(root.left,n1)
   foundN2 = findNode(root.left,n2)
   if(not (foundN1 and foundN2)):
      value = root.value
      return value
   value = findFirstCommonAncestor(n1,n2,root.left,value)
   if(value == None):
      value = findFirstCommonAncestor(n1,n2,root.right,value)
   return value

tree = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

tree.left = one
tree.right = two
one.left = three
one.right = four
two.left = five
two.right = six

print(findFirstCommonAncestor(3,6,tree))