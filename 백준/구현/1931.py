# 1931 회의실 배정
# https://www.acmicpc.net/problem/1931

N = int(input());

arr = [];
possible = [];
max_meeting = 0;

for i in range(N):
    tmp = list(map(int, input().split()));
    arr.append(tmp);
    
arr.sort(key= lambda x : x[0]); # 시작 시간 순서대로 정렬
arr.sort(key =lambda x : x[1]) # 그 상태에서 끝나는 시간순서로 정렬
# 그러면 시작 시간이 빠르면서 끝나는 시간이 빠른 순. (정렬에선 시작시간이 끝나는 시간보다 우선순위)

# print(arr);
start = arr[0];
possible.append(start);
arr.remove(arr[0]);
next = start;
for i in arr:
    if next[1] <= i[0]:
        next = i;
        possible.append(next);

# print(possible)
print(len(possible))
    
    
    
