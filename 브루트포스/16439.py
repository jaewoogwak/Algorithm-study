# 16439 치킨치킨치킨
# https://www.acmicpc.net/problem/16439
import itertools

N, M = list(map(int, input().split()));
c = [];
for i in range(M):
    c.append(i);
prefer = [];
max_list = [];
c_list = list(itertools.combinations(c, 3));
# print(c_list)

for i in range(N):
    tmp = list(map(int, input().split()));
    prefer.append(tmp);
# print(prefer)
p_sum = 0;
max_p = 0;
for i in c_list:
    p_sum = 0;
    for j in range(N):
        p =0;
        for k in range(3):        
            p = max(p, prefer[j][i[k]])
        # print(prefer[j], p, i);    
        p_sum = p_sum + p;
    # print(p_sum)
    if max_p < p_sum:
        max_p = p_sum;
print(max_p);
