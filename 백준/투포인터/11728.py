# 11728 배열 합치기
# https://www.acmicpc.net/problem/11728
import sys;

N,M = map(int, input().split());
arr1 =[];
arr2 = [];

arr1 = list(map(int, sys.stdin.readline().split()));
arr2 = list(map(int, sys.stdin.readline().split()));

newArr= arr1 + arr2;
newArr.sort();

for i in newArr:
    print(i, end=' ');    
# for i in range(M):
#     tmp = int(input());
#     arr2.append(tmp);    
