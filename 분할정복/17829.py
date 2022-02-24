# 17829 222-풀링
# https://www.acmicpc.net/problem/17829

n = int(input());
arr = [ list(map(int, input().split())) for _ in range(n)]

global result;
result = 0;
def sol(ary:list, n):
    second = [];
    next = [];
    tmp = [];
    global result;
    for i in range(0,n):
        for j in range(0, n):
            if i % 2 == 0 and j % 2 == 0:
                tmp.append(ary[i][j]);
                tmp.append(ary[i][j+1]);
                tmp.append(ary[i+1][j]);
                tmp.append(ary[i+1][j+1]);
                tmp.sort(reverse=True);
                second.append(tmp[1]);
                tmp = [];
        # print(second)
        if i % 2 == 0:
            next.append(second);
            second = [];
    # print('next', next);
    n = n //2;
    if n > 1:
        sol(next, n);
    else:
        result = next[0][0];
        return next[0][0];
sol(arr, n);
print(result);
