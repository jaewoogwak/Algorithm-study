import sys
 
 
def CountSum(n, nums):
  if n < 0: return 0
  elif n == 0: return 1
  count = 0
  for x in nums:
    # print(x)
    count += CountSum(n - x, nums)
   
  return count
   
 
T = int(sys.stdin.readline())
for _ in range(T):
  M,N = map(int, sys.stdin.readline().split())
  # print(M,N)
  arr = list(map(int, sys.stdin.readline().split()))
  # print(arr)
  print(CountSum(M, arr))