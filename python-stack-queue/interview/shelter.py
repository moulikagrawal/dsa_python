class Queue:
   def __init__(self):
      self.queue = []

   def __str__(self):
      values = [x for x in self.queue]
      return "\t".join(values)

   def enqueue(self,animal):
      self.queue.append(animal)

   def dequeueAny(self):
      self.queue.pop(0)
   
   def dequeueCat(self):
         for i in range(len(self.queue)):
            if(self.queue[i] == "Cat"):
               self.queue.pop(i)
               break
            i -= 1

   def dequeueDog(self):
         for i in range(len(self.queue)):
            if(self.queue[i] == "Dog"):
               self.queue.pop(i)
               break
            i -= 1
   
   
queue = Queue()
queue.enqueue("Dog")
queue.enqueue("Dog")
queue.enqueue("Cat")
queue.enqueue("Dog")
queue.enqueue("Cat")
print(queue)
queue.dequeueCat()
queue.dequeueDog()
print(queue)