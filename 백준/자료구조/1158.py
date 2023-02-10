# 1158 요세푸스 문제
# https://www.acmicpc.net/problem/1158

num = list(map(int, input().split()));
N = num[0];
K = num[1];

# 1 2 4 5 7
# 0 1 2 3 4 
arr = [];
index = [];
sol = [];
for i in range(N):
    arr.append(i+1);
    index.append(i);
count = 1;
idx= 0; # 첫번째 인덱스 가리킴
while(arr):
    for i in range(K-1):
        idx +=1;
        if idx > len(arr) - 1:
            # K 번째 수의 인덱스가 배열 크기보다 커지면 다시 처음으로 오게 만들기
            idx = 0;    
    tmp = idx;
    sol.append(arr[index[idx]]);
    arr.remove(arr[index[idx]]);
    index.pop();
    if idx + 1 > len(arr):
        idx = 0;
        
print('<', end='');
print(*sol, sep=', ', end='')
print('>', end=''); 
