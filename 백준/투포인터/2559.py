# 2559 수열
import sys;
N,K = list(map(int, input().split()));
arr= list(map(int, sys.stdin.readline().split()));

prefix_sum = [0];
summary = 0;
R = 0;
L = 0;

for i in range(N):
    summary += arr[i]
    prefix_sum.append(summary);
    
# print(prefix_sum)
max_temp = sum(arr[:K]);
# print('maxtemp', max_temp)
for i in range(1, N-K+2):
    L = i;
    R = L+K-1;
    if max_temp < prefix_sum[R]-prefix_sum[L-1]:
        max_temp = prefix_sum[R]-prefix_sum[L-1];
    # print('L :', L, 'R :',R,'까지의 합 :', prefix_sum[R]-prefix_sum[L-1]);
    
print(max_temp)
