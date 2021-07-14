import math

def bubbleSort(list):
   for i in range(len(list)):
      for j in range(len(list)-i-1):
         if(list[j] > list[j+1]):
            list[j],list[j+1] = list[j+1],list[j]
   return list

def buckSort(list):
   numberOfBuckets = round(math.sqrt(len(list)))
   maxValue = max(list)
   arr = []

   for i in range(numberOfBuckets):
      arr.append([])

   for i in range(len(list)):
      index = math.ceil(list[i] * numberOfBuckets/maxValue)
      if(index == 0):
         arr[0].append(list[i])
      else:
         arr[index-1].append(list[i])
   
   for i in range(numberOfBuckets):
      arr[i] = bubbleSort(arr[i])

   k = 0
   for i in range(numberOfBuckets):
      for j in range(len(arr[i])):
         list[k] = arr[i][j]
         k += 1
   
   return list

def bucketSort(list):
   negList = []
   posList = []

   for i in range(len(list)):
      if(list[i] < 0):
         negList.append(-1 * list[i])
      else:
         posList.append(list[i])

   negList = buckSort(negList)
   negList = negList[::-1]
   for i in range(len(negList)):
      negList[i] = -1 * negList[i]
   posList = buckSort(posList)

   return negList + posList

print(bucketSort([-3,6,1,0,9,-2,8,-4,7,-5])) 



   
