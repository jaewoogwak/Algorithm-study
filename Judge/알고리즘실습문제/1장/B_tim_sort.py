# 정렬
# https://judge.koreatech.ac.kr/problem.php?cid=1092&pid=1

import sys
 
MIN_MERGE = 8
 
# 최소 런을 구하는 함수, 배열의 길이를 인자로 받음
def calcMinRun(n):
  r = 0
  # 배열의 길이가 MIN_MERGE보다 클 경우
  while n >= MIN_MERGE:
    r |= n & 1 # 비트연산, n & 1은 n의 가장 오른쪽 비트가 1일 경우 1을, 아니면 0이됨. 결국 n&1의 결과와 n의 비트 OR 연산의 결과가 r에 저장.
    n >>= 1 # n의 비트를 오른쪽으로 1만큼 시프트
  # print("n",n,"r",r)
  # 만약 n이 최소 런보다 작다면 그냥 n을 사용
  return n + r
 
 
# 삽입 정렬, left부터 right 범위까지 정렬함.
def insertionSort(arr, left, right):
  for i in range(left + 1, right + 1):
    j = i # 인덱스 j에 해당하는 값이 key
    while j > left and arr[j] < arr[j - 1]:
      arr[j], arr[j - 1] = arr[j - 1], arr[j]
      j -= 1
 
 
# 정렬된 run들을 병합하는 함수, 만약 배열의 길이가 최소 런보다 작다면 병합 과정은 진행되지 않고 삽입 정렬만 진행됨.
def merge(arr, l, m, r):
  # 입력 받은 배열은 left, right로 나눠짐 
  len1, len2 = m - l + 1, r - m
  left, right = [], []
  for i in range(0, len1):
    left.append(arr[l + i])
  for i in range(0, len2):
    right.append(arr[m + 1 + i])
   
  i, j, k = 0, 0, l
 
  # 나눴던 두 배열을 병합
  while i < len1 and j < len2:
    if left[i] <= right[j]:
      arr[k] = left[i]
      i += 1
 
    else:
      arr[k] = right[j]
      j += 1
 
    k += 1
 
  # 남아있는 요소 붙이기 
  while i < len1:
    arr[k] = left[i]
    k += 1
    i += 1
 
  while j < len2:
    arr[k] = right[j]
    k += 1
    j += 1
 
 
# 팀 정렬 함수
def timSort(arr):
  n = len(arr)
  # 최소 런을 계산
  minRun = calcMinRun(n) 
 
  # 최소 런 단위로 부분 배열을 정렬할건데, 최소 런보다 배열 길이가 작으면 그냥 배열 전체를 삽입 정렬함.
  for start in range(0, n, minRun):
    end = min(start + minRun - 1, n - 1)
    insertionSort(arr, start, end)
 
  size = minRun
  while size < n:
 
    for left in range(0, n, 2 * size):
 
      # 중간값과 끝값을 구해줌.
      mid = min(n - 1, left + size - 1)
      right = min((left + 2 * size - 1), (n - 1))
 
      if mid < right:
        merge(arr, left, mid, right)
 
    size = 2 * size
 
 
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    timSort(arr)
    print(*arr)