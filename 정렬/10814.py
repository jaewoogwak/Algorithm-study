# 10814 나이순 정렬
# https://www.acmicpc.net/problem/10814

N = int(input());
arr = [];

for i in range(N):
    xy = list(input().split());
    arr.append([int(xy[0]), xy[1]]);

# print(arr);    
arr.sort(key=lambda x : x[0]);

for i in arr:
    print('{} {}'.format(i[0], i[1]));
