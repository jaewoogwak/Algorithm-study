# 1715 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import sys
import heapq

sys.stdin = open("test.txt","rt")

N = int(sys.stdin.readline())
hq = []
total = 0

for i in range(N):
  heapq.heappush(hq, int(sys.stdin.readline()))

# 카드를 두 묶음씩 빼 주기
while len(hq) > 1:
  first = heapq.heappop(hq)
  second = heapq.heappop(hq)
  
  dump = first + second
  total += dump
  heapq.heappush(hq, dump)  
  
print(total)