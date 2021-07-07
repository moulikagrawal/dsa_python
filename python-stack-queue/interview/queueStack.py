class Queue:
   def __init__(self):
      self.stack1 = []
      self.stack2 = []
   
   def __str__(self):
      values = [str(x) for x in self.stack1]
      return "\t".join(values)

   def enqueue(self,value):
      self.stack1.append(value)
   
   def dequeue(self):
      self.stack2 = self.stack1.copy()
      self.stack2.reverse()
      self.stack2.pop()
      self.stack1 = self.stack2.copy()
      self.stack1.reverse()

queue = Queue() 
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)
queue.dequeue()
print(queue)