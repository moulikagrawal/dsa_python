class Queue:
   def __init__(self,size):
      self.queue = size * [None]
      self.start = -1
      self.top = -1
      self.size = size

   def __str__(self):
      values = []
      for i in range(self.start,len(self.queue)):
         if(self.queue[i] == None):
            break
         values.append(str(self.queue[i]))
      return "\t".join(values)

   def isEmpty(self):
      if(self.top == -1):
         return True
      return False

   def isFull(self):
      if((self.top + 1 == self.start) or 
         (self.start == 0 and self.top + 1 == self.size)):
         return True
      return False

   def enqueue(self,value):
      if(self.isFull()):
         print("Queue is full")
      else:
         if(self.top + 1 == self.size):
            self.top = 0
         else:
            if(self.start == -1):
               self.start += 1
            self.top += 1
         self.queue[self.top] = value
   
   def dequeue(self):
      if(self.isEmpty()):
         print("Queue is Empty")
      else:
         self.queue[self.start] = None
         if(self.start == self.top):
            self.top = -1
            self.start = -1
         elif(self.start + 1 == self.size):
            self.start = 0
         else:
            self.start += 1

   def peep(self):
      if(self.isEmpty()):
         return "Queue is Empty"
      return self.queue[self.start]

   def deleteQueue(self):
      self.queue = self.size * [None]
      self.start = -1
      self.top = -1
      print("Queue has been deleted")
         
queue = Queue(4)
print(queue.isFull())
queue.enqueue(1)
queue.enqueue(2)
# queue.enqueue(3)
queue.enqueue(4)
print(queue)
print("-------")
queue.dequeue()
queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
queue.enqueue(5)
print(queue)
# print("-------")
# print(queue.peep())
# print("-------")
# queue.deleteQueue()
# print(queue)