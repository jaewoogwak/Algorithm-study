# 2108 통계학
# https://www.acmicpc.net/problem/2108

import sys;
N = int(sys.stdin.readline());
data = [];

frequency2 = {}
for i in range(8002): # -4001 ~ 4001
    frequency2[i-4001] = 0;
for i in range(N):
    n = int(sys.stdin.readline());
    data.append(n);

# 산술평균
v1 = sum(data) / N
v1= round(v1);
v1= int(v1);

# 중앙값
tmp = list(map(int, data));
tmp.sort();
v2 = tmp[int((N+1)/2) - 1];

# 최빈값
prev = 0;
for i in data:
    frequency2[i] += 1;

def max_fq (x):
    return frequency2[x];

first_fq_key = max(frequency2.keys(), key=max_fq);
first_fq_value= frequency2[first_fq_key];
del frequency2[first_fq_key];
second_fq_key = max(frequency2.keys(), key=max_fq);
second_fq_value = frequency2[second_fq_key];
if first_fq_value == second_fq_value:
    v3 = second_fq_key;
else: v3 = first_fq_key;


# 범위
max_num = max(data);
min_num = min(data);
v4 = max_num - min_num;

print(v1);
print(v2);
print(v3);
print(v4);
