# 10025 게으른 백곰
# https://www.acmicpc.net/problem/10025

N,K = list(map(int,input().split()));
bucket = dict();

for i in range(N):
    t = list(map(int, input().split()));
    bucket[t[1]] = t[0];

for i in range(max(bucket)):
    if i not in bucket:
        bucket[i] = 0;
bucket = dict(sorted(bucket.items()))

start = 0;
end = 0;
interval_sum =0;
max_sum = 0;
# print(bucket)
for start in range(len(bucket)):
    while(end <= start+(2*K) and end < len(bucket)):
        interval_sum = interval_sum + bucket[end];
        # print('sum : ', interval_sum, 'start :', start, 'end : ', end)
        end = end + 1;
    if interval_sum > max_sum:
        max_sum = interval_sum;
    interval_sum = interval_sum - bucket[start];
        
print(max_sum)
