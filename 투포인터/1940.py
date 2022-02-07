# 1940 주몽
# https://www.acmicpc.net/problem/1940
import sys;

N = int(input());
M = int(input());

arr = list(map(int, sys.stdin.readline().split()));
arr = sorted(arr);

start = 0;
end = 1;
two_sum = 0;
count = 0;
# print(arr);
for start in range(N):
    while two_sum < M and end < N:
        two_sum = arr[start] + arr[end];
        # print(arr[start], arr[end], start, end);
        end = end + 1;
    if two_sum == M:
        count +=1;
    two_sum = 0;
    end = start+2;
print(count)
    
         
