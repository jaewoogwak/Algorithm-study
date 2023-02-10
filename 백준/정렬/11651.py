# 11651 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651

N = int(input());

location = [];

for i in range(N):
    loc = list(map(int, input().split()));
    location.append([loc[0], loc[1]]);
    
location.sort(key = lambda x : x[0])
location.sort(key =lambda x : x[1]);

for i in location:
    print(i[0], i[1])
