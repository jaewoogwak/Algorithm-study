# 20053
# https://www.acmicpc.net/problem/20053

T = int(input());
arr = [];
max_num =0;
min_num =0;
for i in range(T):
    N = int(input());
    arr = list(map(int, input().split()));
    max_num= max(arr);
    min_num = min(arr);
    print(min_num, max_num);
