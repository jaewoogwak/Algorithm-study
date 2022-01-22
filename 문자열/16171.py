# 16171 나는 친구가 적다
# https://www.acmicpc.net/problem/16171

S = input();
K = input();
arr =[];
for i in S:
    if i != '0' and i != '1' and i!='2' and i!='3' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9':
        arr.append(i);

string = ''.join(arr);

if K in string:
    print(1)
else:print(0);
