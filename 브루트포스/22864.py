# 22864 피로도
# https://www.acmicpc.net/problem/22864

# a : 피로도
# b : 처리할 일
# c : 줄어드는 피로도
# m : 번아웃 기준

tmp = list(map(int, input().split()));
A = tmp[0];
B = tmp[1];
C = tmp[2];
M = tmp[3];

work = 0;
fatigue = 0;

for i in range(24):
    # 피로도가 한계치보다 낮을때
    if fatigue + A <= M:
        work += B;
        fatigue += A;
    # 피로도가 한계치보다 높을때
    else:
        fatigue -= C;
    if fatigue < 0:
            fatigue = 0;
        
        
print(work);
