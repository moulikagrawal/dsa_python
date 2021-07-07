class Stack_List:
   def __init__(self):
      self.stack_list = []
      self.min = []

   def __str__(self):
      # self.stack_list.reverse()
      reversed_list = self.stack_list.copy()
      reversed_list.reverse()
      values = [str(x) for x in reversed_list]
      return "\t".join(values)
   
   def mine(self):
      if(self.min):
         return self.min[-1]
      return None

   def isEmpty(self):
      if(self.stack_list == []):
         return True
      else:
         return False

   def push(self,value):
      if(self.min == []):
         self.min.append(value)
      if(self.min and self.min[-1] > value):
         self.min.append(value)
      self.stack_list.append(value)

   def pop(self):
      if self.isEmpty():
         return "Stack is empty"
      else:
         val = self.stack_list.pop()
         if(self.min and self.min[-1] == val):
            self.min.pop()
         return val

   def delete(self):
      self.stack_list = []

stack = Stack_List()
stack.push(1)
stack.push(-2)
print(stack.mine())
stack.push(-5)
# print(stack)
print(stack.mine())
stack.pop()
print(stack.mine())
# stack.delete()
# print(stack)


