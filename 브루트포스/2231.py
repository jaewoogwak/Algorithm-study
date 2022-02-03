# 2231 분해합
# https://www.acmicpc.net/problem/2231

N = int(input());
is_exist = False;
k =0;

for i in range(N):
    num = i;
    summary = 0;
    while(num >= 10):
        k = int(num % 10);
        summary += k;
        num = int(num / 10);
    summary += num;
    if(summary + i == N):
        print(i);
        is_exist = True;
        break;
    
if(is_exist == False):
    print(0)
