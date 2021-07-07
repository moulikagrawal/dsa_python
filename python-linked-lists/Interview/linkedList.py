from random import randint
class Node:
   def __init__(self,value):
      self.value = value
      self.next = None
      self.prev = None

   def __str__(self):
      return str(self.value)

class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None
   
   def __iter__(self):
      node = self.head
      while node:
         yield node.value
         node = node.next

   def __str__(self):
      values = [str(node) for node in self]
      return " -> ".join(values)

   def __len__(self):
      tempNode = self.head
      length = 0
      while tempNode:
         length += 1
         tempNode = tempNode.next
      return length

   def add(self,value):
      newNode = Node(value)
      if(self.head == None):
         self.head = newNode
         self.tail = newNode
      else:
         self.tail.next = newNode
         self.tail = newNode

   def generate(self,length,minValue,maxValue):
      for i in range(length):
         self.add(randint(minValue,maxValue))
      return self

   # def removeDup(self):
   #    tempNode = self.head
   #    while(tempNode):
   #       if tempNode.value not in {x for x in newLinkedList}:
   #          newLinkedList.add(tempNode.value)
   #       tempNode = tempNode.next

   def removeDup(self):
      tempNode = self.head
      values = {tempNode.value}
      while(tempNode.next):
         if(tempNode.next.value in values):
            tempNode.next = tempNode.next.next
         else:
            values.add(tempNode.next.value)
            tempNode = tempNode.next


linkedList = LinkedList()
# newLinkedList = LinkedList()
# print(linkedList.generate(5,1,1))
# linkedList.removeDup()
# print(linkedList)
# print(len(linkedList))