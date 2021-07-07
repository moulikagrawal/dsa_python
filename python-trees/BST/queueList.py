class Node:
   def __init__(self,value=None):
      self.value = value
      self.next = None
   
class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def __iter__(self):
      node = self.head
      while(node):
         yield node
         node = node.next

class Queue:
   def __init__(self):
      self.list = LinkedList()

   def __str__(self):
      values = [str(x.value) for x in self.list]
      return "\t".join(values)

   def isEmpty(self):
      if(self.list.head == None):
         return True
      return False

   def enqueue(self,value):
      node = Node(value)
      if(self.list.head == None):
         self.list.head = node
         self.list.tail = node
      else:
         self.list.tail.next = node
         self.list.tail = node

   def dequeue(self):
      if(self.isEmpty()):
         print("Queue is empty")
      else:
         dequedElement = self.list.head
         if(self.list.head == self.list.tail):
            self.list.head = None
            self.list.tail = None
         else:      
            self.list.head = self.list.head.next
         return dequedElement

   def peek(self):
      if(self.isEmpty()):
         print("Queue is empty")
      else:
         return self.list.head.value

   def deleteQueue(self):
      self.list.head = None
      self.list.tail = None

queue = Queue()