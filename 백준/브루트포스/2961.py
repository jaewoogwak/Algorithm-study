# 2961 도영이가 만든 맛있는 음식
# https://www.acmicpc.net/problem/2961
import itertools

N = int(input());
S=[];
B=[];
c_list = [];

for i in range(N):
    sb = input().split();
    S.append(int(sb[0]));
    B.append(int(sb[1]));
    # 재료는 최소 한개, 한 번씩만 사용 => 조합
    t = list(itertools.combinations(range(N),i+1));
    c_list += t;
#print(c_list)
min_gap = 1000000000;
for case in c_list:
    gap = 0;
    s_taste= 1;
    b_taste=0;
    # print('case');
    for i in range(len(case)):
        # print(case[i]);
        s_taste *= S[case[i]];
        b_taste += B[case[i]];
    
    if s_taste >= b_taste:
        gap = s_taste -b_taste;
    else: gap = b_taste - s_taste;
    # print('gap', gap, 's_taste', s_taste, 'b_taste', b_taste);    
    min_gap = min(gap, min_gap)
print(min_gap)
