class Node:
   def __init__(self,value):
      self.value = value
      self.prev = None
      self.next = None

class DoublyLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None
   
   def __iter__(self):
      node = self.head
      while node:
         yield node.value
         node = node.next
   
   def createDoublyLinkedList(self):
      node = Node(1)
      self.head = node
      self.tail = node

   def insert(self,value,location):
      newNode = Node(value)
      if(location == 0):
         newNode.next = self.head
         self.head.prev = newNode
         self.head = newNode
      elif(location == -1):         
         newNode.prev = self.tail
         self.tail.next = newNode
         self.tail = newNode
      else:
         index = 1
         tempNode = self.head
         while(index < location - 1):
            tempNode = tempNode.next
            index += 1
         newNode.prev = tempNode
         newNode.next = tempNode.next
         tempNode.next.prev = newNode
         tempNode.next = newNode     
   
   def traverse(self):
      tempNode = self.head
      while tempNode is not None:
         print(tempNode.value)
         tempNode = tempNode.next

   def reverseTraverse(self):
      tempNode = self.tail
      while tempNode is not None:
         print(tempNode.value)
         tempNode = tempNode.prev

   def search(self,value):
      tempNode = self.head
      loc = 1
      while tempNode is not None:
         if(tempNode.value == value):
            return "Value found at location " + str(loc)
         loc += 1
         tempNode = tempNode.next
      return "Value cannot be found"

   def delete(self,location):
      if(location == 0):
         if(self.head == self.tail):
            self.head = None
            self.tail = None
         else:
            self.head.next.prev = None
            self.head = self.head.next
      elif(location == -1):
         if(self.head == self.tail):
            self.head = None
            self.tail = None
         else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
      else:
         index = 1
         tempNode = self.head
         while(index < location - 1):
            tempNode = tempNode.next
            index += 1
         tempNode.next.next.prev = tempNode
         tempNode.next = tempNode.next.next

   def deleteFullDoublyLinkedList(self):
      tempNode = self.head
      while(tempNode is not None):
         tempNode.prev = None
         tempNode = tempNode.next
      self.head = None
      self.tail = None


linkedList = DoublyLinkedList()
linkedList.createDoublyLinkedList()
linkedList.insert(0,0)
linkedList.insert(2,-1)
linkedList.insert(3,-1)
linkedList.insert(4,-1)
linkedList.insert(10,3)
linkedList.insert(12,6)
linkedList.insert(5,-1)
print([node for node in linkedList])
# linkedList.traverse()
# linkedList.reverseTraverse()
# print(linkedList.search(55))
# linkedList.deleteFullDoublyLinkedList()
linkedList.delete(3)
linkedList.delete(5)
print([node for node in linkedList])
