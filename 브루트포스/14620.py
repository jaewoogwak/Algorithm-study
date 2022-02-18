# 14620 꽃길
# https://www.acmicpc.net/problem/14620

import itertools
import sys
N =int(input());
arr = [];
for i in range(N):
    t = list(map(int, sys.stdin.readline().split()));
    arr.append(t);
    
dx = [0,0,0,-1,1];
dy = [0,1,-1,0,0];
ary = [];
for i in range(N):
    for j in range(N):
        if i!=0 and  j!=0 and i!=N-1 and j!=N-1:
            ary.append((i,j));
# print('ary', ary)

# 3개의 꽃이 필 수 있는 좌표 조합 구하기
c_list = list(itertools.combinations(ary, 3))
# print('clist', c_list, len(c_list))

min_cost = 200*5*3;
for c in c_list:
    checked = [[0]*N for _ in range(N)];
    total_cost = 0;
    for i in range(3):
        x = c[i][0];
        y = c[i][1];
        is_possible = True;
        cost = 0;
        # 씨앗을 심은 좌표를 기준으로 꽃이 피면(상하좌우 좌표) 다른 꽃과 안 겹치는지 확인
        for k in range(5):
            if checked[x+dx[k]][y+dy[k]] == 1:
                # 상하좌우 확인하다가 이미 꽃이 핀 자리랑 겹치면 바로 break
                is_possible = False;
                break;
        # 위 조건을 통과했을때, 비로소 상하좌우 + 씨앗 심어진 곳 5개 좌표의 땅값을 더함.
        # 그리고 꽃이 피었다고 체크 (checked에 추가)
        if is_possible == True:
            for k in range(5):
                # cost : 꽃 하나가 핀 자리의 땅값의 합
                cost += arr[x+dx[k]][y+dy[k]];
                checked[x+dx[k]][y+dy[k]] = 1;
            # total_cost : cost 3개를 합해서 3가지 꽃이 핀 자리들의 땅값의 합
            total_cost += cost;
        else: break;
    if is_possible == True:
        # print('조합', c[0], c[1],c[2])
        # for i in checked:
            # print(i);
        # print('total_cost', total_cost);
        # 위 조건들을 만족했을 때의 꽃이 피는 3개의 자리 조합의 땅값의 합에서 최솟값 구하기
        min_cost = min(total_cost, min_cost)
        # print('min_cost', min_cost)
print(min_cost)
