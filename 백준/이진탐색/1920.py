# 1920 수 찾기
# https://www.acmicpc.net/problem/1920
import sys;

N = int(input());
arr= list(map(int, sys.stdin.readline().split()));

M = int(input());
m_list = list(map(int, sys.stdin.readline().split()));

arr.sort();
for i in m_list:
    is_exist = False;
    target = i;
    left = 0;
    right = N-1;
    while left <= right:
        mid = (left+right) // 2;
        if arr[mid] == target:
            print(1);
            is_exist = True;
            break;
        elif target < arr[mid]:
            right = mid - 1;
        elif target > arr[mid]:
            left = mid + 1;
    if is_exist == False:
        print(0);
