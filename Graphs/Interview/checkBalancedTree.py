class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def helper(root):
   if(not root):
      return 0
   leftHeight = helper(root.left)
   rightHeight = helper(root.right)
   if(abs(leftHeight - rightHeight) > 1):
      return -1
   
   return max(leftHeight,rightHeight) + 1

def isBalanced(root):
   return helper(root) > -1

# def height(root):
#    if(not root):
#       return 0
#    if(root.left == None and root.right == None):
#       return 1
#    else:
#       heightLeft = 1 + height(root.left)
#       heightRight = 1 + height(root.right)
#       if(heightRight > heightLeft):
#          return heightRight
#       return heightLeft

# def isBalanced(root):
#    if(not root):
#       return True
#    heightLeft = height(root.left)
#    heightRight = height(root.right)
#    result = True
#    diff = heightLeft - heightRight
#    if(diff != 0 and diff != 1 and diff != -1):
#       result = False
#       return result
#    result = isBalanced(root.left)
#    if(result == True):
#       result = isBalanced(root.right)
#    return result

tree = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)

tree.left = two
tree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven
six.left = eight
# eight.left = nine

print(isBalanced(tree))