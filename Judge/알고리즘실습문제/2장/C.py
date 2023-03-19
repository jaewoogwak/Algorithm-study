import sys
 
 
def HowSum(n, nums):  
  if n < 0: return None
  elif n == 0:
    return []
  for x in nums:
    list = HowSum(n - x, nums)
    if list is not None:
      list.append(x)
      return list
  return None
   
 
T = int(sys.stdin.readline())
for _ in range(T):
  M,N = map(int, sys.stdin.readline().split())
  # print(M,N)
  arr = list(map(int, sys.stdin.readline().split()))
  # print(arr)
  lst = HowSum(M, arr)
  if lst == None:
    print(-1)
     
  elif len(lst) > 0:
    print(len(lst), *lst)
 
  else:
    print(0)