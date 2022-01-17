# 11650 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

N = int(input());
arr = [];

for i in range(N):
    xy = list(map(int, input().split()));
    arr.append(xy);
    
arr.sort();

for i in arr:
    print('{} {}'.format(i[0], i[1]));
