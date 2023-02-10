# 1935 후위 표기식2
# https://www.acmicpc.net/problem/1935

N = int(input());
exp = input();
arr = [];
for i in range(N):
    n = int(input());
    arr.append(n);

stk = [];
idx = 0;
for i in exp:
    if i.isalpha() == True:
        stk.append(arr[ord(i)-ord('A')]);
    else:
        optr = i;
        num2 = stk.pop();
        num1 = stk.pop();
        if optr == '+':
            v = num1 + num2;
            stk.append(v);
        elif optr == '-':
            v = num1 - num2;
            stk.append(v);
        elif optr == '*':
            v = num1 * num2;
            stk.append(v);
        elif optr == '/':
            v = num1 / num2;
            stk.append(v);
    # print(stk)

print('%.2f' %stk[0]);
