# 2775 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775

import sys

sys.stdin = open("test.txt","rt")

T = int(input())

dp = [[i for i in range(1,16)] for i in range(15)]

for i in range(1,15):
  for j in range(15):
    if j == 0:
      dp[i][j] = 1
    else:
      dp[i][j] = dp[i-1][j] + dp[i][j-1]


for _ in range(T):
  k = int(input())
  n = int(input())
  print(dp[k][n-1])  
  
  
  