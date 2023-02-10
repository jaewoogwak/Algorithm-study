# 10815 숫자카드
# https://www.acmicpc.net/problem/10815
import sys;

N = int(sys.stdin.readline());
card = list(map(int, sys.stdin.readline().split()));
M = int(sys.stdin.readline());
num = list(map(int, sys.stdin.readline().split()));

isExist = [];
index= 0;

card.sort();
def BS(target : int):
    low = 0;
    high = len(card) -1;
    while(low <= high):
        mid = int((low + high) / 2);
        if card[mid] == target:
            return mid;
        elif card[mid] > target:
            high = mid-1;
        else: low = mid +1;
    # 발견 못했을때
    return -1;
    


for i in num:
    x = BS(i);
    if x == -1:
        isExist.append(0);
    else: isExist.append(1);
   
for i in isExist:
    print(i, end=' ')
        
