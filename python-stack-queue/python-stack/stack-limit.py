class Stack_Limit_list:
   def __init__(self,size):
      self.stack_list = []
      self.size = size

   def __str__(self):
      reversed_list = self.stack_list.copy()
      values = [str(x) for x in reversed_list]
      return "\t".join(values)

   def isEmpty(self):
      if(self.stack_list == []):
         return True
      return False
   
   def isFull(self):
      if(len(self.stack_list) == self.size):
         return True
      return False

   def push(self,value):
      if(self.isFull()):
         print("Stack is Full.. Element cannot be added")
      else:
         print("Element is pushed onto the stack")
         self.stack_list.append(value)

   def pop(self):
      if(self.isEmpty()):
         print("Stack is empty")
      else:
         print("Element is popped from the stack")
         self.stack_list.pop()

   def peek(self):
      return self.stack_list[-1]

   def delete(self):
      self.stack_list = []

stack = Stack_Limit_list(3)
stack.push(1)
print(stack.peek())
stack.push(2)
stack.push(3)
stack.push(7)
print(stack.peek())
stack.pop()
stack.pop()
# stack.pop()
# stack.pop()
print(stack)
# stack.delete()
# print(stack)