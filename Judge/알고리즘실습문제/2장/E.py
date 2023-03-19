import sys
 
 
def best_sum(m, arr):
  if m < 0:
    return None
   
  elif m == 0:
    return []
   
  best = None
   
  for x in arr:
    list = best_sum(m - x, arr)
 
    if list != None:
       
      if best == None or len(best) > len(list) + 1:
        list.append(x)
        best = list
 
  return best
 
   
 
T = int(sys.stdin.readline())
for _ in range(T):
  M,N = map(int, sys.stdin.readline().split())
  arr = list(map(int, sys.stdin.readline().split()))
 
  ans = best_sum(M, arr)
  if ans == None:
    print("-1")
   
  elif len(ans) == 0:
    print("0")
   
  else:
    print(len(ans), *ans)