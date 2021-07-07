class Node:
   def __init__(self,value):
      self.value = value
      self.next = None

class Stack_Linkedlist: 
   def __init__(self):
      self.head = None

   def __str__(self):
      node = self.head
      values = []
      while(node):
         values.append(str(node.value))
         node = node.next
      return "\t".join(values)

   def isEmpty(self):
      if(self.head) == None:
         return True
      return False
   
   def push(self,value):
      node = Node(value)
      if(self.head == None):
         self.head = node
      else:
         node.next = self.head
         self.head = node
   
   def pop(self):
      if(self.isEmpty()):
         print("Stack is empty")
      else:
         self.head = self.head.next
      
   def peek(self):
      if(self.head):
         return self.head.value
      return "Stack is empty"

   def delete(self):
      self.head = None

stack = Stack_Linkedlist()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
# print(stack)
# stack.pop()
# print(stack)
print(stack.peek())
stack.delete()
print(stack)