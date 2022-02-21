# 2630 색종이 만들기
# https://www.acmicpc.net/problem/2630

import sys;
N = int(input());
paper = [ list(map(int, input().split())) for _ in range(N)]
result = []; # 색종이 넣는 배열

def sol(x,y,n):
    num = paper[x][y]; # 첫 번째 색종이와 다른 모든 색종이가 같아야함
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != paper[i][j]:
                # 첫 번째 색종이와 다를 경우 범위를 가로세로 1/2로 줄여서 (4분할)
                # 다시 재귀함수 넣기
                sol(x,y, n // 2);
                sol(x, y+n//2, n//2);
                sol(x+n//2, y, n//2);
                sol(x+n//2, y+n//2, n//2);
                return;
    # 범위를 줄이고 줄여서 결국 첫 번째 색종이와 
    # 다른 색종이가 다 같을 경우에 갯수 세기
    if num == 0:
        result.append(0);
    else:
        result.append(1); 

sol(0,0,N);
print(result.count(0));
print(result.count(1));
