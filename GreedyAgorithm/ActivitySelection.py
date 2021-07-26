def activitySelection(activites):
   activites.sort(key=lambda a: a[2])
   i = 0
   first = activites[i][0]
   print(first)
   for j in range(len(activites)):
      if(activites[j][1] > activites[i][2]):
         print(activites[j][0])
         i = j

activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
            ]
activitySelection(activities)