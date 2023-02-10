# 2346 풍선 터뜨리기
# https://www.acmicpc.net/problem/2346
from collections import deque
import sys;

N = int(input());
q = deque(enumerate(map(int, input().split())));
ans = [];
# print(q);
while q:
    idx,num = q.popleft();
    ans.append(idx+1);
    if num > 0:
        q.rotate(-(num-1));
    elif num <0:
        q.rotate(-num);
    # print(q);
print(' '.join(map(str, ans)));
