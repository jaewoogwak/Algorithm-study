import sys
import math
 
 
def getDistance(posOne, posTwo):
  return math.sqrt((posOne[0] - posTwo[0])*(posOne[0] - posTwo[0]) + (posOne[1] - posTwo[1])*(posOne[1] - posTwo[1]))
 
 
def bruteforceClosestPair(arr):
  min = 100000000001
  ret = [0,0]
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      d = getDistance(arr[i], arr[j])
       
      if min > d:
        min, ret[0], ret[1] = d, arr[i], arr[j]
   
  return ret
       
 
# posX: x축을 기준으로 오름차순 정렬
# posY: y축을 기준으로 내림차순 정렬
def closestPair(Px, Py):
  if len(Px) <= 3:
    return bruteforceClosestPair(Px)
   
  else:
    mid = len(Px) // 2
    Lx = Px[:mid]
    Rx = Px[mid:]
    Ly = sorted(Lx, key=lambda point: point[1])
    Ry = sorted(Rx, key=lambda point: point[1])
 
    l1, l2 = closestPair(Lx, Ly)
    r1, r2 = closestPair(Rx, Ry)
    minimumDistance = min(getDistance(l1, l2), getDistance(r1, r2))
     
    if getDistance(l1, l2) > getDistance(r1, r2):
      bestPair = r1, r2
       
    else:
      bestPair = l1, l2
       
    ret = closestSplitPair(Px, Py, minimumDistance, bestPair)
   
    return ret
 
def closestSplitPair(Px, Py, d, bestPair):
  mid = len(Px) // 2
  x_bar = Px[mid][0]
  Sy = [p for p in Py if x_bar - d <= p[0] <= x_bar + d]
  best = d
 
  for i in range(len(Sy) - 1):
    for j in range(1, min(7, len(Sy) - i)):
      if getDistance(Sy[i], Sy[i+j]) < best:
        best = getDistance(Sy[i], Sy[i+j])
        bestPair = (Sy[i], Sy[i+j])
         
  return bestPair
 
 
def generateInputPair():
  temp = list(map(int, sys.stdin.readline().split()))
  arr = []
  for i in range(0, len(temp), 2):
    arr.append((temp[i], temp[i+1]))
     
  return arr
 
 
def main():
  T = int(sys.stdin.readline())
  for _ in range(T):
    N = int(sys.stdin.readline())
    arr = generateInputPair()
    p1, p2 = closestPair(sorted(arr, key=lambda pos:pos[0]), sorted(arr, key=lambda pos:pos[1]))
     
    answer = getDistance(p1, p2)
    print(f'{answer:.2f}')
   
 
main()