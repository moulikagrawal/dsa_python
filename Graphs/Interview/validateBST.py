class TreeNode:
     def __init__(self, value):
         self.val = value
         self.left = None
         self.right = None

def isValidBST(root):
    if(not root):
        return True
    result = True
    if(root.left is None or root.right is None):
        return True
    if(root.val > root.left.val):
        result = isValidBST(root.left)
    else:
        result = False
        return result
    if(result == True):
        if(root.val < root.right.val):
            result = isValidBST(root.right)
        else:
            result = False
            return result

    return result

tree = TreeNode(5)
three = TreeNode(3)
two = TreeNode(2)
four = TreeNode(4)
seven = TreeNode(7)
six = TreeNode(6)
eight = TreeNode(8)

tree.left = three
three.left = two
three.right = four
tree.right = seven
seven.left = eight
seven.right = six

print(isValidBST(tree))
