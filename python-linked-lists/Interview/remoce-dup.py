tempNode = self.head
while(tempNode):
   nextNode = tempNode.next
   prevNode = tempNode
   while(nextNode):
      if(tempNode.value = nextNode.value):
         prevNode.next = nextNode.next
      nextNode = nextNode.next
      prevNode = prevNode.next
   
   