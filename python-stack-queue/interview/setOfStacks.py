import math

class setOfStacks:
   def __init__(self,stackSize):
      self.stackSize = stackSize
      self.list = []

   def __str__(self):
      values = [str(x) for x in self.list]
      return "\t".join(values)

   def popAt(self,stackNum):
      self.list[stackNum].pop()

   def push(self,value):
      if(self.list and len(self.list[-1]) < self.stackSize):
         self.list[-1].append(value)
      else:
         self.list.append([value])

   def pop(self):
      if(self.list[-1]):
         self.list[-1].pop()
      else:
         self.list.pop()
         self.list[-1].pop()

st = setOfStacks(4)
print(st)
# print(st.stacks)
st.push(1)
# print(st.stacks)
st.push(1)
st.push(1)
st.push(1)
st.push(1)
# st.pop())
# st.pop()
print(st)
st.popAt(0)
print(st)
# print(st.stacks)