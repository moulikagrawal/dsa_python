class Node:
   def __init__(self,value):
      self.value = value
      self.prev = None
      self.next = None
   
class CircularDoublyLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None
   
   def __iter__(self):
      node = self.head
      while node:
         yield node.value
         if(node.next == self.head):
            break
         node = node.next
   
   def createCircularDoublyLinkedList(self):
      node = Node(1)
      self.head = node
      self.tail = node
      node.prev = node
      node.next = node

   def insert(self,value,location):
      newNode = Node(value)
      if(location == 0):
         newNode.next = self.head
         newNode.prev = self.tail
         self.head.prev = newNode
         self.tail.next = newNode
         self.head = newNode
      elif(location == -1):
         newNode.prev = self.tail
         newNode.next = self.head
         self.head.prev = newNode
         self.tail.next = newNode
         self.tail = newNode
      else:
         tempNode = self.head
         index = 1
         while(index < location - 1):
            tempNode = tempNode.next
            index += 1
         newNode.prev = tempNode
         newNode.next = tempNode.next
         tempNode.next.prev = newNode
         tempNode.next = newNode

   def traverse(self):
      tempNode = self.head
      while(1):
         print(tempNode.value)
         tempNode = tempNode.next
         if(tempNode == self.head):
            break
   
   def reverseTraverse(self):
      tempNode = self.tail
      while(1):
         print(tempNode.value)
         tempNode = tempNode.prev
         if(tempNode == self.tail):
            break

   def search(self,value):
      tempNode = self.head
      loc = 1
      while(1):
         if(tempNode.value == value):
            return "Value found at location " + str(loc)
         tempNode = tempNode.next
         loc += 1
         if(tempNode == self.head):
            break
      return "Value cannot be found"

   def delete(self,location):
      if(location == 0):
         if(self.head == self.tail):
            self.head.next = None
            self.head.prev = None
            self.tail = None
            self.head = None
         else:
            self.head.next.prev = self.tail
            self.tail.next = self.head.next
            self.head = self.head.next
      elif(location == -1):
         if(self.head == self.tail):
            self.head.next = None
            self.head.prev = None
            self.tail = None
            self.head = None
         else:
            self.tail.prev.next = self.head
            self.head.prev = self.tail.prev
            self.tail = self.tail.prev
      else:
         index = 1
         tempNode = self.head
         while(index < location - 1):
            tempNode = tempNode.next
            index += 1 
         tempNode.next.next.prev = tempNode
         tempNode.next = tempNode.next.next 

   def deleteFullCircularDoublyLinkedList(self):
      tempNode = self.head
      while(1):
         tempNode.prev = None
         tempNode = tempNode.next
         if(tempNode == self.head):
            break
      self.tail.next = None
      self.head = None
      self.tail = None

linkedList = CircularDoublyLinkedList()
linkedList.createCircularDoublyLinkedList()
linkedList.insert(0,0)
linkedList.insert(4,0)
linkedList.insert(2,-1)
linkedList.insert(3,-1)
linkedList.insert(5,2)
linkedList.insert(6,4)
print([node for node in linkedList])
# linkedList.traverse()
# linkedList.reverseTraverse()
print(linkedList.search(13))
# linkedList.delete(-1)
# linkedList.deleteFullCircularDoublyLinkedList()
# print([node for node in linkedList])
