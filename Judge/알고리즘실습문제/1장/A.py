# 서로 다른 문자로 구성된 길이가 3인 부분문자열 수
# https://judge.koreatech.ac.kr/problem.php?cid=1092&pid=0

import sys
from collections import deque
 
T = int(sys.stdin.readline())
 
# 슬라이딩 윈도우 함수, 인자로 문자열과 구간 길이를 입력받고 길이가 k인 좋은 부분문자열 수를 반환한다.
def sliding_window(str, k):
  # 길이가 k인 좋은 부분문자열 수
  count = 0
  # 시작 인덱스 0으로 초기화
  start = 0
  # 슬라이당 윈도우 기법이 우측으로 이동함에 따라 요소가 왼쪽에서 빠져나가고 오른쪽으로 들어오는 것에 따라 덱 사용
  dq = deque() 
   
  # end는 문자열 str에서 인덱스 값을, val은 문자열 str에서 end 인덱스에 해당하는 값임
  for end, val in enumerate(str): 
    # 덱에 val을 계속해서 넣어줌
    dq.append(val) 
    # 그러다가 구간 길이가 3일 때 좋은 부분문자열인지 확인
    if end - start + 1 == k: 
      # 만약 3개 문자가 모두 다르다면 좋은 부분문자열이므로 count 1 증가
      if dq[0] != dq[1] and dq[1] != dq[2] and dq[0] != dq[2]: #
        count += 1
      # 이제 창문이 오른쪽으로 넘어가듯이, 덱에서 왼쪽 요소 하나 pop
      dq.popleft()
      # 그리고 오른쪽 요소를 덱에 넣기 위해 start를 1 증가
      start += 1
   
  return count
 
for _ in range(T):
  str = sys.stdin.readline().rstrip()
  print(sliding_window(str, 3))
  