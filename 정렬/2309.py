# 2309 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

arr = [];
for i in range(9):
    N = int(input());
    arr.append(N);
    
tmp = [];
res = [];
# [20, 7, 23, 19, 10, 15, 25, 8, 13]

tmp = list(arr);
for i in tmp:
    tmp = list(arr);
    for j in tmp:
        if(i!=j):
            tmp = list(arr);
            tmp.remove(i);
            tmp.remove(j);
            if 100 == sum(tmp):
                res = list(tmp);
res.sort();

for i in res:
    print(i);
