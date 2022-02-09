# 10799 쇠막대기
import sys;
arr = sys.stdin.readline();

stk = [];

count = 0;
for i in range(len(arr)-1):
    if arr[i] == '(':
        stk.append('(');
    
    else:
        # arr[i] == ')'
        if arr[i-1] == '(':
            # 레이저인 경우
            stk.pop();
            count += len(stk);
            # print(count, len(stk));
        else:
            # 막대기 끝일 경우
            count += 1;
           
            stk.pop();
print(count);   
