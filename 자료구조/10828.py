# 10828 스택
# https://www.acmicpc.net/problem/10828

import sys;
N = int(input())

stk = [];

for i in range(N):
    cmd = sys.stdin.readline().strip();
    # print(cmd)
    if 'push' in cmd:
        num = 0;
        tmp = "";
        for j in range(5, len(cmd)):
            tmp += cmd[j];
        stk.append(tmp)
    elif 'pop' in cmd:
        if len(stk) == 0:
            print(-1);
        else:
            tmp = stk[-1];
            stk.pop()
            print(tmp);
    elif 'top' in cmd:
        if len(stk) == 0:
            print(-1);
        else:print(stk[-1]);
    elif 'size' in cmd:
        print(len(stk));
    elif 'empty' in cmd:
        if len(stk) == 0:
            print(1);
        else: print(0);
    
