import sys

N,r,c = list(map(int, input().split()))

ans = 0


while N != 0:
  N -= 1
  
  # 1사분면
  if r < 2 ** N and c < 2 ** N:
    ans += 0 * (2 ** N) * (2 ** N)
  
  # 2사분면
  elif r < 2 ** N and c >= 2 ** N:
    ans += 1 * (2 ** N) * (2 ** N)
    c -= (2 ** N)
    
  # 3사분면
  elif r >= 2 ** N and c < 2 ** N:
    ans += 2 * (2 ** N) * (2 ** N)
    r -= (2 ** N)
  
  # 4사분면
  else:
    ans += 3 * (2 ** N) * (2 ** N)
    r -= (2 ** N)
    c -= (2 ** N)
    
print(ans)
    
