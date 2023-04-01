import sys
 
 
def CountSum(n, nums):
  if n < 0: return 0
  
  elif n == 0: return 1
  
  count = 0
  for x in nums:
    count += CountSum(n - x, nums)
    
  return count


def main():
  T = int(sys.stdin.readline())
  for _ in range(T):
    M,N = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    print(CountSum(M, arr))
    
    
main()