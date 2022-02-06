# 1966 프린터 큐
# https://www.acmicpc.net/problem/1966
from collections import deque;

T = int(input());

for i in range(T):
    N, M = list(map(int, input().split()));
    tmp = deque(list(map(int, input().split())));
    k = 0;
    importance = deque();
    for j in tmp:
        importance.append([j, k])
        k+=1;
    # print(importance)
    count = [];
    while(len(importance) > 0):
        # print('max', max(importance))
        if importance[0][0] >= max(importance)[0]:
            v = importance.popleft();
            count.append(v[1])
            # print(v);
        else:
            v = importance.popleft();
            importance.append(v);
            # print(importance)
            
        if len(importance) == 0:break;
    c = 1;
    for j in count:
        if j == M:
            print(c)
            break;
        c+=1;
            
