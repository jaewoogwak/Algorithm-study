# 10866 덱
# https://www.acmicpc.net/problem/10866

import sys;
from collections import deque;

N = int(input());
dq = deque();

for i in range(N):
    cmd = sys.stdin.readline();
    if 'push_back' in cmd:
        num = cmd[10:len(cmd)+1];
        num = int(num);
        dq.append(num);
    elif 'push_front' in cmd:
        num = cmd[10:len(cmd)+1];
        num = int(num);
        dq.appendleft(num);
    elif 'pop_front' in cmd:
        if len(dq) == 0:
            print(-1);
        else:
            num = dq.popleft();
            print(num)
    elif 'pop_back' in cmd:
        if len(dq) == 0:
            print(-1);
        else:
            num = dq.pop();
            print(num);
    elif 'size' in cmd:
        print(len(dq));
    elif 'empty' in cmd:
        if len(dq) == 0:
            print(1);
        else: print(0);
    elif 'front' in cmd:
        if len(dq) == 0:
            print(-1);
        else: print(dq[0]);
    elif 'back' in cmd:
        if len(dq) == 0:
            print(-1);
        else: print(dq[-1]);
    
