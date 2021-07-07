# numbers = list()
# for i in range(1,11):
#    numbers.append(i)

nums=[1,2,3,4,5,7,8,9,10]
numbers = (10*11)/2
missingNumber = numbers - sum(nums)

print("Missing number is : " + str(int(missingNumber)))