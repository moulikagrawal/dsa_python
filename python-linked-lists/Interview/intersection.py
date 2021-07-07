# To check if intersection is there just check the 
# last node reference..if that is same then two linked lists intersect

from linkedList import LinkedList,Node

def intersect(linkedList1,linkedList2):
   tempNode1 = linkedList1.head
   tempNode2 = linkedList2.head
   index = 0
   length1 = len(linkedList1)
   length2 = len(linkedList2)
   if(length1 > length2):
      longer = linkedList1.head
      shorter = linkedList2.head
      start = length1 - length2
   else:
      longer = linkedList2.head
      shorter = linkedList1.head
      start = length2 - length1
   
   for i in range(start):
      longer = longer.next

   while(shorter is not longer):
      shorter = shorter.next
      longer = longer.next
   
   return longer
def addSameNode(linkedList1,linkedList2,value):
   linkedList1.add(value)
   linkedList2.add(value)

linkedList1 = LinkedList()
linkedList2 = LinkedList()
linkedList1.generate(5,1,90)
linkedList2.generate(7,1,90)
addSameNode(linkedList1,linkedList2,11)
addSameNode(linkedList1,linkedList2,14)
print(linkedList1)
print(linkedList2)
print(intersect(linkedList1,linkedList2))