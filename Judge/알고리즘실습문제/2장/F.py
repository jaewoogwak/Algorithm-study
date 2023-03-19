import sys


def isEven(num):
  if num % 2 == 0:
    return True
  
  else:
    return False
  
def solve(m):
  global numCount
  ret = []
  C = []
  find(m, ret, C)
  
  ans = []
  for c in ret:
    ans.append(c[0]*100 + c[1]*10 + c[2])
    
  return ans


def find(m, ret, C):
  if m == 0:
    if isEven(C[0]*100 + C[1]*10 + C[2]) and C[0] != 0:
      ret.append(C[:])
      return
  
  else:
    for i in range(0, 10):
      if numCount[i] > 0:
        C.append(i)
        numCount[i] -=1
        find(m - 1, ret, C)
        C.pop()
        numCount[i] +=1


T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())
  arr = list(map(int, sys.stdin.readline().split()))
  numCount = [0] * 10

  for n in arr:
    numCount[n] += 1 

  print(*solve(3))


