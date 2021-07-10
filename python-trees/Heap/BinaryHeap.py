class Heap:
   def __init__(self,size):
      self.heapList = size * [None]
      self.heapSize = 0
      self.maxSize = size 

   def peek(self):
      if(not self.heapList):
         return
      return self.heapList[1]

   def sizeOfHeap(self):
      if(not self.heapList):
         return
      return self.heapSize

   def heapify(self,index,heapType):
      parentIndex = int(index/2)
      if(index == 1):
         return
      if(heapType == "Min"):
         if(self.heapList[index] < self.heapList[parentIndex]):
            temp = self.heapList[index]
            self.heapList[index] = self.heapList[parentIndex]
            self.heapList[parentIndex] = temp
         self.heapify(parentIndex,heapType)
      elif(heapType == "Max"):
         if(self.heapList[index] > self.heapList[parentIndex]):
            temp = self.heapList[index]
            self.heapList[index] = self.heapList[parentIndex]
            self.heapList[parentIndex] = temp
         self.heapify(parentIndex,heapType)

   def insertHeap(self,value,heapType):
      if(self.heapSize + 1 == self.maxSize):
         print("Heap is full")
      else:
         self.heapList[self.heapSize + 1] = value
         self.heapSize += 1
         self.heapify(self.heapSize,heapType)
         print("Value has been inserted successfully")

   def heapifyExtract(self,index,heapType):
      leftIndex = index * 2
      rightIndex = index * 2 + 1

      if(self.heapSize < leftIndex):
         return
      elif(self.heapSize == leftIndex):
         if(heapType == "Min"):
            if(self.heapList[index] < self.heapList[leftIndex]):
               temp = self.heapList[leftIndex]
               self.heapList[leftIndex] = self.heapList[index]
               self.heapList[index] = temp
         elif(heapType == "Max"):
            if(self.heapList[index] > self.heapList[leftIndex]):
               temp = self.heapList[leftIndex]
               self.heapList[leftIndex] = self.heapList[index]
               self.heapList[index] = temp
         return
      else:
         if(heapType == "Min"):
            if(self.heapList[leftIndex] < self.heapList[rightIndex]):
               swap = leftIndex
            else:
               swap = rightIndex
            temp = self.heapList[swap]
            self.heapList[swap] = self.heapList[index]
            self.heapList[index] = temp

         elif(heapType == "Max"):
            if(self.heapList[leftIndex] > self.heapList[rightIndex]):
               swap = leftIndex
            else:
               swap = rightIndex
            temp = self.heapList[swap]
            self.heapList[swap] = self.heapList[index]
            self.heapList[index] = temp
         
         self.heapifyExtract(swap,heapType)

   def extractNode(self,heapType):
      if(self.heapSize == 0):
         print("Empty Heap")
      else:
         self.heapList[1] = self.heapList[self.heapSize]
         self.heapList[self.heapSize] = None
         self.heapSize -= 1
         self.heapifyExtract(1,heapType)

   def deleteHeap(self):
      self.heapList = None
      self.heapSize = 0

   def levelOrder(self):
      if(self.heapSize == 0):
         print("\nEmpty Heap")
      else:
         for i in range(1,self.heapSize+1):
            print(self.heapList[i],end=" ")

   def preOrder(self,index):
      if(index > self.heapSize):
         return
      else:
         print(self.heapList[index],end=" ")
         self.preOrder(2*index)
         self.preOrder(2*index+1)

   def inOrder(self,index):
      if(index > self.heapSize):
         return
      else:
         self.inOrder(2*index)
         print(self.heapList[index],end=" ")
         self.inOrder(2*index+1)
   
   def postOrder(self,index):
      if(index > self.heapSize):
         return
      else:
         self.postOrder(2*index)
         self.postOrder(2*index+1)
         print(self.heapList[index],end=" ")

heap = Heap(10)
heap.insertHeap(10,"Min")
heap.insertHeap(2,"Min")
heap.insertHeap(20,"Min")
heap.insertHeap(5,"Min")
heap.levelOrder()

heap.extractNode("Min")
print("\n")
heap.levelOrder()

# heap.deleteHeap()
# heap.levelOrder()