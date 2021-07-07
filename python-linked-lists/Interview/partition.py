from linkedList import LinkedList

# def partition(num,linkedList):
#    tempNode = linkedList.head
#    while(tempNode):
#       if(tempNode.value < num):
#          linkedList1.add(tempNode.value)
#       else:
#          linkedList2.add(tempNode.value)
#       tempNode = tempNode.next
   
#    linkedList1.tail.next = linkedList2.head

# def partition(num,linkedList):
#    tempNode = linkedList.head
#    values = []
#    while(tempNode):
#       if(tempNode.value < num):
#          values.append(tempNode.value)
#       tempNode = tempNode.next

#    tempNode = linkedList.head
#    while(tempNode):
#       if(tempNode.value > num):
#          values.append(tempNode.value)
#       tempNode = tempNode.next
   
#    tempNode = linkedList.head
#    i = 0
#    while(tempNode):
#       tempNode.value = values[i]
#       i += 1
#       tempNode = tempNode.next

def partition(self,linkedList):
   currentNode = self.head
   linkedList.tail = self.head

   while(currentNode):
      if()

linkedList = LinkedList()
# linkedList1 = LinkedList()
# linkedList2 = LinkedList()
print(linkedList.generate(10,1,100))
partition(50,linkedList)
print(linkedList)