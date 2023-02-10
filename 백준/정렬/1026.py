# 1026 보물
# https://www.acmicpc.net/problem/1026

N = int(input());

arr1 = list(map(int, input().split()));
arr2 = list(map(int, input().split()));
newArr = [];
arr1.sort();
newArr= list(map(int, arr1));

S = 0;

for i in newArr:
    max_num = max(arr2);
    S = S + max_num * i;
    arr2.remove(max_num);
print(S)
        
