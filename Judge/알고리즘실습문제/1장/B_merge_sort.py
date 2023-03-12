# 정렬
# https://judge.koreatech.ac.kr/problem.php?cid=1092&pid=1

import sys
 
# 병합 정렬, 정렬할 리스트를 인자로 받는다
def merge_sort(arr):
  # sort 함수, mid값을 갱신함. 직접적인 정렬은 merge 함수에서 이루어짐.
  def sort(low, high):  
    if high - low < 2: # 리스트의 길이가 1 이하라면 중단
      return
    mid = (low + high) // 2
    sort(low, mid) # low에서 mid까지 리스트 나누기
    sort(mid, high) # mid에서 high전까지 리스트 나누기
    merge(low, mid, high) # low에서 mid까지, mid에서 high 전까지 정렬
 
  # merge 함수, low에서 high전까지(range(low, high)) 정렬함 
  def merge(low, mid, high): 
    temp = [] # 부분 정렬을 하기 위한 임시 리스트
    l, h = low, mid
 
    # l이 mid보다 작고 h가 high보다 작은 상태에서 작은 값부터 temp에 삽입
    while l < mid and h < high:
      if arr[l] < arr[h]: # arr[l]이 arr[h]보다 작으면 arr[l]을 임시 리스트에 추가
        temp.append(arr[l])
        l += 1 # 추가한 후 해당 인덱스 값 1 증가
      else: # 그렇지 않다면 arr[h]를 임시 리스트에 추가
        temp.append(arr[h])
        h += 1 # 추가한 후 해당 인덱스 값 1 증가
 
    # 아직 남아있는 원소가 있으면 나머지 원소를 임시 리스트에 추가
    while l < mid: 
      temp.append(arr[l])
      l += 1
    while h < high:
      temp.append(arr[h])
      h += 1
 
    # low부터 high전까지 기존 배열애서 인덱스를 조정하여 정렬(in-place)
    for i in range(low, high):
      arr[i] = temp[i - low] # i-low를 해줌으로써 항상 임시배열의 0번째 인덱스부터 접근 가능
 
  return sort(0, len(arr))
   
   
T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())
  arr = list(map(int, sys.stdin.readline().split()))
  merge_sort(arr)
  print(*arr)
  
  
# merge_sort 함수의 공간복잡도를 알아보자.
# 외부 입력으로 주어지는 길이가 N인 arr은 len(arr) = N으로 어떤 알고리즘 구현 방식에 관계없이 같은 입력 크기를 가진다. 
# 따라서 내부에서 메모리를 얼마나 사용하는지에 주목할 필요가 있다.
# merge_sort 함수에서는 부분 정렬을 하기 위한 임시 리스트 temp 하나만 사용한다.
# 입력으로 주어진 arr의 인덱스를 조정하여 정렬을 진행하기 때문이다.
# 또한 임시 리스트 temp의 크기는 (mid-l) + (high-h)이다.
# 결국 temp의 최대 크기는 N을 넘지 않으므로 공간 복잡도는 S(N)으로 정의할 수 있다.
# 임시배열 temp를 사용하였기에 완전한 in-place 방식은 아니지만 공간복잡도를 줄이기 위한 좋은 시도라고 생각했다.