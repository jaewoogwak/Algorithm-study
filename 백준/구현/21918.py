# 21918 전구
# https://www.acmicpc.net/problem/21918

arr = list(map(int, (input().split())));

N = arr[0]; # 전구 갯수
M = arr[1] # 명령어 갯수

light = list(map(int, (input().split())));


def order1(i, x):
    light[i-1] = x;

def order2(l,r):
    for i in range(l-1, r):
        if light[i] == 0:
            light[i] = 1;
        else:
            light[i] = 0;

def order3(l,r):
    for i in range(l-1, r):
        light[i] = 0;

def order4(l,r):
    for i in range(l-1, r):
        light[i] = 1;

for i in range(M):
    order = list(map(int, (input().split())));
    if order[0] == 1:
        order1(order[1], order[2]);
    elif order[0] == 2:
        order2(order[1], order[2]);
    elif order[0] == 3:
        order3(order[1], order[2]);
    elif order[0] == 4:
        order4(order[1], order[2]);
    
for i in light:
    print(i, end=' ');
    
