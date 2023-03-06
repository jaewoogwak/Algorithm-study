# 15903 카드 합체 놀이
# https://www.acmicpc.net/problem/15903

import sys
import heapq

sys.stdin = open("test.txt","rt")

n, m = list(map(int, sys.stdin.readline().split()))
cards = list(map(int, sys.stdin.readline().split()))

cards = sorted(cards)

for i in range(m):
  c1=heapq.heappop(cards)
  c2=heapq.heappop(cards)
  s = c1 + c2
  heapq.heappush(cards, s)
  heapq.heappush(cards, s)
  

print(sum(cards))

