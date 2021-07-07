class Node:
   def __init__(self,value=0):
      self.value = value
      self.next = None

class SLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def __iter__(self):
      node = self.head
      while node:
         yield node.value
         node = node.next

   def insert(self,value,location):
      newNode = Node(value)
      if(self.head == None):
         self.head = newNode
         self.tail = newNode
      else:
         if(location == 0):
            newNode.next = self.head
            self.head = newNode
         elif(location == -1):
            self.tail.next = newNode
            self.tail = newNode
         else:
            index = 1
            tempNode = self.head
            while(index < location - 1):
               tempNode = tempNode.next
               index += 1
            nextNode = tempNode.next
            newNode.next = nextNode
            tempNode.next = newNode

   def traversal(self):
      node =  self.head
      while node is not None:
         print(node.value)
         node = node.next

   def delete(self,location):
      if(self.head is None):
         print("List is Empty")
      else:
         if(location == 0):
            if(self.head == self.tail):
               self.head = None
               self.tail = None
            else:
               self.head = self.head.next
         
         elif(location == -1):
            if(self.head == self.tail):
               self.head = None
               self.tail = None
            else:
               tempNode = self.head
               while tempNode.next != self.tail:
                  tempNode = tempNode.next
               tempNode.next = None
               self.tail = tempNode
         
         else:
            index = 1
            tempNode = self.head
            while(index < location - 1):
               tempNode = tempNode.next
               index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next


linkedList = SLinkedList()
linkedList.insert(0,0)
linkedList.insert(1,-1)
linkedList.insert(2,-1)
linkedList.insert(3,-1)
linkedList.insert(5,2)

print([node for node in linkedList])
# linkedList.traversal()
linkedList.delete(3)
print([node for node in linkedList])