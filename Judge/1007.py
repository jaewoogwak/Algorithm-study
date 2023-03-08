# 1007 유일한 수
# https://judge.koreatech.ac.kr/problem.php?id=1007

import sys

sys.stdin = open("test.txt","rt")

T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  arr = list(map(int,sys.stdin.readline().split()))
  
  check = {}
  
  for v in arr:
    if v in check:
      check[v] += 1
    else:
      check[v] = 1


  print(check, arr)
  for v in arr:
    if check[v] == 1:
      print(v)
      break  