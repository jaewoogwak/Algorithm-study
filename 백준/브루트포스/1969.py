# 1969 DNA
# https://www.acmicpc.net/problem/1969
from collections import deque;
N, M = list(map(int, input().split()));

count = 0;
dna = [];

result = [];
compare = [];

for i in range(N):
    d = input();
    tmpd = [];
    for j in d:
        tmpd.append(j);
    dna.append(tmpd);

for i in range(M):
    tmp = deque();
    max_count = 0;
    for j in range(N):
        tmp.append(dna[j][i]);
        tmp = sorted(tmp);
    compare.append(tmp);
    for j in tmp:
        if max_count < tmp.count(j):
            max_count = tmp.count(j); 
            d = j;
    result.append(d);


for i in range(M):
    for j in range(N):
        if result[i] != compare[i][j]:
            count +=1;

for i in result:
    print(i, end='');
print()
print(count)
