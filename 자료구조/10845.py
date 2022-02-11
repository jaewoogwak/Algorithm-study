# 10845 큐
# https://www.acmicpc.net/problem/10845
from collections import deque
import sys;
q = deque();

N = int(input());

for i in range(N):
    cmd = sys.stdin.readline();
    if 'push' in cmd:
        num =""
        for j in range(5, len(cmd)):
            num += str(cmd[j]);
        num = int(num);
        q.append(num);
    elif 'pop' in cmd:
        if len(q) == 0:
            print(-1);
        else:
            num = q.popleft();
            print(num);
    elif 'size' in cmd:
        print(len(q));
    elif 'empty' in cmd:
        if len(q) == 0:
            print(1);
        else: print(0);
    elif 'front' in cmd:
        if len(q) == 0:
            print(-1);
        else:
            print(q[0]);
    elif 'back' in cmd:
        if len(q) == 0:
            print(-1);
        else:
            print(q[-1]);
    
