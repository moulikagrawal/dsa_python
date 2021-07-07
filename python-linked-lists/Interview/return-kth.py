from linkedList import LinkedList

def returnkth(num,linkedList):
   index = 1
   location = len(linkedList) - num + 1
   tempNode = linkedList.head
   while(index < location):
      tempNode = tempNode.next
      index += 1
   return str(location - 1) + "th element from last is --> " + str(tempNode.value)

# def returnkth(num,linkedList):
#    pointer1 = linkedList.head
#    pointer2 = linkedList.head
#    index = 1
#    while(index < num):
#       pointer2 = pointer2.next
#       index += 1
#    while(pointer2.next):
#       pointer1 = pointer1.next
#       pointer2 = pointer2.next
#    return str(num) + " element from last is --> " + str(pointer1.value)


linkedList = LinkedList()
print(linkedList.generate(10,1,100))
print(returnkth(5,linkedList))