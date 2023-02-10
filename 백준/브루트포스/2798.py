# 2798 블랙잭
# https://www.acmicpc.net/problem/2798

card = list(map(int, input().split()));
N = card[0];
M = card[1];

num = list(map(int, input().split()));
sum = 0;
max_sum = 0;
for i in num:
    for j in num:
        for k in num:
            if i != j and j!= k and i!=k:
                if i + j + k <= M:
                    sum = i + j + k;
                    if max_sum < sum:
                        max_sum = sum;
                                                
print(max_sum)
