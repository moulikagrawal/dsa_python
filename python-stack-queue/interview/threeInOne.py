class MultiStack:
   def __init__(self,stackSize,totalStack):
      self.stackSize = stackSize
      self.totalStack = totalStack
      self.list = [0] * (stackSize * totalStack)
      self.sizes = [0] * totalStack

   def __str__(self):
      values = [str(x) for x in self.list]
      return "\t".join(values)
   
   def indexAtTop(self,stackNum):
      offset = stackNum * self.stackSize
      return offset + self.sizes[stackNum] - 1
   
   def isEmpty(self,stackNum):
      if(self.sizes[stackNum] == 0):
         return True
      return False
   
   def isFull(self,stackNum):
      if(self.sizes[stackNum] == self.stackSize):
         return True
      return False
      
   def push(self,value,stackNum):
      if(self.isFull(stackNum)):
         print("Stack is full")
      else:
         self.list[self.indexAtTop(stackNum) + 1] = value
         self.sizes[stackNum] += 1
   
   def pop(self,stackNum):
      if(self.isEmpty(stackNum)):
         print("Stack is empty")
      else:
         self.list[self.indexAtTop(stackNum)] = 0
         self.sizes[stackNum] -= 1

   def peek(self,stackNum):
      if(self.isEmpty(stackNum)):
         print("Stack is empty")
      else:
         return self.list[self.indexAtTop(stackNum)]
      
stack = MultiStack(3,4)
print(stack)
print(stack.isEmpty(1))
stack.push(1,1)
stack.push(2,1)
stack.push(3,1)
stack.pop(1)
print(stack)
print(stack.isFull(1))

   
   
