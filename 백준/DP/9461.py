# 9461 파도반 수열
# https://www.acmicpc.net/problem/9461

import sys

sys.stdin = open("test.txt","rt")

dp = [0] * 101
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2

for i in range(5, 101):
  dp[i] = dp[i-1] + dp[i-5]

T = int(input())

for _ in range(T):
  N = int(input())
  print(dp[N])