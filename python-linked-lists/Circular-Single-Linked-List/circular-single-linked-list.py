class Node:
   def __init__(self,value=0):
      self.value = value
      self.next = None

class CSingleLinkedList:
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

   def insert(self,value,location):
      newNode = Node(value)
      if(location == 0):
         newNode.next = self.head
         self.head = newNode
         self.tail.next = newNode
      
      elif(location == -1):
         self.tail.next = newNode
         newNode.next = self.head
         self.tail = newNode
      
      else:
         index = 1
         tempNode = self.head
         while index < location - 1:
            tempNode = tempNode.next
            index += 1
         newNode.next = tempNode.next
         tempNode.next = newNode

   def traverse(self):
      tempNode = self.head
      while tempNode:
         print(tempNode.value)
         if(tempNode.next == self.head):
            break
         tempNode=tempNode.next

   def search(self,value):
      tempNode = self.head
      location = 1
      while 1:
         if(tempNode.value == value):
            return "Value is found at location " + str(location)
         tempNode = tempNode.next
         location += 1
         if(tempNode == self.head):
            return "Value cannot be found"

   def delete(self,location):
      if(location == 0):
         if(self.head == self.tail):
            self.head.next = None
            self.head = None
            self.tail = None
         else:
            self.head = self.head.next
            self.tail.next = self.head
      elif(location == -1):
           if(self.head == self.tail):
            self.head.next = None
            self.head = None
            self.tail = None
            
           else:
               tempNode = self.head
               while(tempNode.next != self.tail):
                  tempNode = tempNode.next
               tempNode.next = self.head
               self.tail = tempNode
      else:
         tempNode = self.head
         index = 1
         while(index < location - 1):
            tempNode = tempNode.next
            index += 1
         tempNode.next = tempNode.next.next

linkedList = CSingleLinkedList()
node1 = Node(1)
linkedList.head = node1
linkedList.tail = node1
node1.next = node1

linkedList.insert(0,0)
linkedList.insert(2,0)
linkedList.insert(7,-1)
linkedList.insert(9,-1)
linkedList.insert(8,-1)
linkedList.insert(6,5)
print([node for node in linkedList])
# linkedList.traverse()
# print(linkedList.search(8))
linkedList.delete(-1)
linkedList.delete(0)
linkedList.delete(0)
print([node for node in linkedList])
