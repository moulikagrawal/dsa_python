from linkedList import LinkedList
import math

def summ(linkedList1,linkedList2):
   # total = 0
   # tempNode = linkedList.head
   # i = 0
   # while(tempNode):
   #    total = (tempNode.value * pow(10,i)) + total
   #    tempNode = tempNode.next
   #    i += 1
   # return total

   # tempNode1 = linkedList1.head
   # tempNode2 = linkedList2.head
   # finalList = LinkedList()
   # carry = 0
   # while(tempNode1 or tempNode2):
   #    if(tempNode1 and tempNode2):
   #       total = tempNode1.value + tempNode2.value + carry
   #    elif(tempNode1):
   #        total = tempNode1.value + carry
   #    else:
   #        total = tempNode2.value + carry
   #    if(total > 10):
   #       finalList.add(total % 10)
   #       carry = 1
   #    elif(total == 10):
   #       finalList.add(0)
   #       carry = 1
   #    else:
   #       finalList.add(total)
   #       carry = 0

   #    if(tempNode1):
   #       tempNode1 = tempNode1.next
   #    if(tempNode2):
   #       tempNode2 = tempNode2.next

   # if(carry == 1):
   #    finalList.add(1)
   # return finalList

   tempNode1 = linkedList1.head
   tempNode2 = linkedList2.head
   carry = 0
   while(tempNode1 or tempNode2):
      total = 0 + carry
      if(tempNode1):
         total = total + tempNode1.value
         tempNode1 = tempNode1.next
      if(tempNode2):
         total = total + tempNode2.value
         tempNode2 = tempNode2.next
      if((total / 10) >= 1):
         carry = 1
      else:
         carry = 0
      finalList.add(total % 10)  

   if(carry == 1):
      finalList.add(1)
   return finalList  


linkedList1 = LinkedList()
linkedList2 = LinkedList()
finalList = LinkedList()
print(linkedList1.generate(3,1,9))
print(linkedList2.generate(3,1,9))
print(summ(linkedList1,linkedList2))