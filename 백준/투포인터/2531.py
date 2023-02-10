# 2531 회전초밥
# https://www.acmicpc.net/problem/2531
import sys
N,d,k,c = list(map(int, sys.stdin.readline().split()));
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# k : 연속해서 먹는 접시 수
# c : 쿠폰번호 (제외할 번호)
start = 0;
end =0;
answer =0;
while start <N:
    end = start + k;
    case = set();
    addable = True;
    for i in range(start, end):
        i %= N;
        case.add(arr[i]);
        if arr[i] == c:
            addable = False;
    cnt = len(case);
    if addable == True:
        cnt +=1;
    answer = max(answer, cnt);
    start+=1;
print(answer)
    
        
