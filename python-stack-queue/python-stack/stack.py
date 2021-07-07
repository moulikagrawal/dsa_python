class Stack_List:
   def __init__(self):
      self.stack_list = []
   
   def __str__(self):
      # self.stack_list.reverse()
      reversed_list = self.stack_list.copy()
      reversed_list.reverse()
      values = [str(x) for x in reversed_list]
      return "\t".join(values)
   
   def isEmpty(self):
      if(self.stack_list == []):
         return True
      else:
         return False

   def push(self,value):
      self.stack_list.append(value)

   def pop(self):
      if self.isEmpty():
         return "Stack is empty"
      else:
         return self.stack_list.pop()

   def delete(self):
      self.stack_list = []

stack = Stack_List()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
stack.pop()
# stack.delete()
print(stack)


