# 5568 카드 놓기
# https://www.acmicpc.net/problem/5568

import itertools;
# n개 중에 k개 뽑고 -> 조합
# 뽑은거에서 줄세우기 -> 순열
n = int(input());
k = int(input());
arr = []
for i in range(n):
    t = int(input());
    arr.append(t);

num_list = [];
c_list=list(itertools.combinations(arr, k));
# print(c_list)
p_list = [];
for i in c_list:
    p_list = p_list + list(itertools.permutations(list(i), len(list(i))));
    
# print(p_list)
for i in p_list:
    num = ""
    for a in i:
        num += str(a);
    if int(num) not in num_list:
        num_list.append(int(num));
    
print(len(num_list));
