# 18511 큰 수 구성하기
# https://www.acmicpc.net/problem/18511

import itertools;

N, K = list(map(int, input().split()));
arr = list(map(int, input().split()))
sol = [];

for i in range(1, len(str(N))+1):
    sol = sol + list(itertools.product(arr, repeat=i));
# print(sol);
num_list = [];
for set in sol:
    num = "";
    for n in set:
        num += str(n);
    num_list.append(int(num));

num_list = sorted(num_list, reverse=True);
    
            
# print(num_list)
for i in num_list:
    if N >= i:
        print(i);
        break;
    
