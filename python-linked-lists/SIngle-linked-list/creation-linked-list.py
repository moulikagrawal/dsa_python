class Node:
   def __init__(self,value=0):
      self.value = value
      self.next = None

class SLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

SingleLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)

node1.next = node2
SingleLinkedList.head = node1
SingleLinkedList.tail = node2 
