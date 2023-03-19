import sys
 
 
def CanSum(n, nums):
  # print(n)
  if n < 0: return False
  elif n == 0: return True
  for x in nums:
    if CanSum(n - x, nums): return True
  return False
 
   
T = int(sys.stdin.readline())
for _ in range(T):
  M,N = map(int, sys.stdin.readline().split())
  # print(M,N)
  arr = list(map(int, sys.stdin.readline().split()))
  # print(arr)
  if (CanSum(M, arr)):
    print("true")
  else:
    print("false")