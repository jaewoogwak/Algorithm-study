# 9012 괄호
# https://www.acmicpc.net/problem/9012

from collections import deque

N = int(input());

for t in range(N):    
    
    tmp = input();
    PS = deque();
    for i in tmp:
        PS.append(i);
    is_end = False;
    while(1):
        # print(PS);
        if len(PS) == 1:
            print('NO');
            break;
        if PS[0] == ')':
            print('NO');
            break;
        for i in PS:
            if i == ')':
                PS.remove(')');
                PS.popleft();
                break;
            if ')' not in PS:
                is_end = True;
                break;
        if is_end == True:
            print('NO');
            break;
        if len(PS) == 0:
            print('YES');
            break;
        
        
