# 11365 !밀비 급일
# https://www.acmicpc.net/problem/11365

while(1):
    a = list(input().split());
    string = ' '.join(a);
    if string=='END':
        break;
    for i in reversed(string):
        print(i, end='')
    print('');
