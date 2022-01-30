# 18258 큐 2
# https://www.acmicpc.net/problem/18258
import sys;
from collections import deque;
N = int(input());

q = deque();

for i in range(N):
    cmd = sys.stdin.readline();
    
    if 'push' in cmd:
        num = "";
        for j in range(5, len(cmd)):
            num += cmd[j];
        num = int(num);
        q.append(num); 
    elif 'pop' in cmd:
        if len(q) == 0:
            print(-1);
        else:
            tmp = q[0];
            q.popleft();
            print(tmp);
    elif 'size' in cmd:
        print(len(q));
    elif 'empty' in cmd:
        if len(q) == 0:
            print(1);
        else: print(0);
    elif 'front' in cmd:
        if len(q) == 0:
            print(-1);
        else: print(q[0]);
    elif 'back' in cmd:
        if len(q) == 0:
            print(-1);
        else: print(q[-1]);
