# 2164 카드 2
# https://www.acmicpc.net/problem/2164
from collections import deque;
N = int(input());
dq = deque();

for i in range(N):
    dq.append(i+1);

# 카드가 한 장일때
if len(dq) == 1:
    print(dq[0]);
else:
    while(1):
        # 제일 위의 카드 버리기
        dq.popleft();
        if len(dq) == 1:
            last_card = dq[0];
            break;
        # 그 다음 카드는 제일 아래로 옮기기
        card = dq.popleft();
        dq.append(card);
    print(last_card)
