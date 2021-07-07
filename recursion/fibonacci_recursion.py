count = 0
fibonacci_list = [0,1]

def fibonacci(a,b,limit):
   global count
   if(count == limit):
      return
   else:
      count += 1
      fibonacci_list.append(a+b)
      fibonacci(b,a+b,limit)

fibonacci(0,1,10)
for i in fibonacci_list:
   print(i," ",end="")

def fib(num):
   if(num in [0,1]):
      return num
   else:
      return fib(num-1) + fib(num-2)


