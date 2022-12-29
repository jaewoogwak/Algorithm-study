import sys

def fibonacci(n):
  global memo
  
  if memo[n][0] != 0:
    return memo[n][0], memo[n][1], memo[n][2]
  
  elif n == 0:
    memo[n][1] += 1
    return 0, 1, 0
  elif n == 1:
    memo[n][2] += 1
    return 1, 0 ,1
  else:
    fib2 = fibonacci(n-2)
    fib1 = fibonacci(n-1)
    memo[n][0] = fib2[0] + fib1[0]
    memo[n][1] += (fib2[1] + fib1[1])
    memo[n][2] += (fib2[2] + fib1[2])
    return memo[n][0], memo[n][1], memo[n][2]
  


T = int(input())

for _ in range(T):
  memo = [[0,0,0] for i in range(41)]
  n = int(input())
  fibonacci(n)
  print(memo[n][1], memo[n][2])
  

