# 3986 좋은 단어
# https://www.acmicpc.net/problem/3986

N = int(input());
count = 0;
arr =[];
for i in range(N):
    tmp =input();
    stk = [];
    for j in range(0, len(tmp)):
        next = tmp[j];
        # print('next', next)
        if len(stk) >= 1:
            if stk[-1] == next:
                stk.pop();
            else:
               stk.append(tmp[j]); 
        else:
            stk.append(tmp[j]);
        
    if len(stk) == 0:
        count +=1;
print(count);
