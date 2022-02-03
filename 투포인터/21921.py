# 21921 블로그
# https://www.acmicpc.net/problem/21921
import sys;
from collections import deque
N,X = map(int, input().split());

people = list(map(int, sys.stdin.readline().split()));
visitor_sum = deque();
prefix_sum = deque();

summary = 0;
prefix_sum = [0];
for i in people:
    summary += i;
    prefix_sum.append(summary);
    
l=0;
r=0;
for i in range(len(prefix_sum)):
    if i+X < len(prefix_sum):
        visitor_sum.appendleft(prefix_sum[i+X] - prefix_sum[i]);
        
print(prefix_sum)
visitor_sum = sorted(visitor_sum, reverse=True);
max_visior_sum = visitor_sum[0];
count =0;
print(visitor_sum)

for i in visitor_sum:
    if max_visior_sum == i:
        count+=1;
    else:break;
        
if max_visior_sum == 0:
    print('SAD');
else:
    print(max_visior_sum);
    print(count);
