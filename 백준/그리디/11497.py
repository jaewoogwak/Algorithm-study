# 11497 통나무 건너뛰기
# https://www.acmicpc.net/problem/11497

import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  logs = list(map(int, sys.stdin.readline().split()))
  
  logs = sorted(logs)
  
  newLogs = deque()

  for i in range(N):
    log = logs.pop()
    if i % 2 == 0:
      newLogs.appendleft(log)
    else: newLogs.append(log)
  
  gap = 0
  for i in range(1, N):
    gap = max(abs(newLogs[i] - newLogs[i-1]), gap)
  gap = max(abs(newLogs[N-1] - newLogs[0]), gap)
  print(gap)
  