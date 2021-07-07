class Queue:
   def __init__(self):
      self.queue = []

   def __str__(self):
      values = [str(x) for x in self.queue]
      return "\t".join(values)

   def isEmpty(self):
      if(self.queue == []):
         return False
      return True
   
   def enqueue(self,value):
      self.queue.append(value)
   
   def dequeue(self):
      if(self.queue == []):
         print("Queue is empty")
      else:
         self.queue.pop(0)
   
   def peek(self):
      if(self.queue == []):
         print(" Queue is empty")
      else:
         print(self.queue[0])
      
   def deleteQueue(self):
      self.queue = []

queue = Queue()
# print(queue.isEmpty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
queue.dequeue()
print(queue)
queue.peek()
queue.deleteQueue()
print(queue)

