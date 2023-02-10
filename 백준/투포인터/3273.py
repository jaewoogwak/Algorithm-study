# 3273 두 수의 합
# https://www.acmicpc.net/problem/3273
import sys;

n = int(input());
arr = list(map(int, sys.stdin.readline().split()));
x = int(input());

arr =sorted(arr);
pair_sum =0;
count =0;
left =0;
right =n-1;

for left in range(len(arr)):
    while(left < right):
        pair_sum = arr[left] + arr[right];
        # print(pair_sum, arr[left], arr[right])
        if pair_sum == x:
            count +=1;
            right-=1;
            break;
        if pair_sum < x:
            break;
        right -=1;
print(count);
