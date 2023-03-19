import sys


# 블럭 생성
def L(r,c, flag):
  if flag == 0:
    return (r,c), (r,c+1), (r+1,c)
  
  elif flag == 1:
    return (r,c), (r, c+1), (r+1, c+1)
  
  elif flag == 2:
    return (r,c), (r+1, c), (r+1, c+1)
    
  else:
    return (r,c), (r+1, c), (r+1, c-1)


# 빈 칸을 세는 함수
def countWhiteCell(H,W, board):  
  whiteCell = 0
  for r in range(H):
    for c in range(W):
      if board[r][c]:
        whiteCell += 1

  return whiteCell


# 판을 블록 하나로 덮고 나서 남아있는 다음 흰 칸을 찾는 함수
def findNextWhiteCell(H, W, board, startR, startC):
  for r in range(H):
    for c in range(W):
      if board[r][c]:
        return r,c

  return -1,-1


# 블록을 놓을 수 있는지 확인하는 함수(범위 체크)
def canPutBlock(r,c):
  if r == -1 or c == -1 or r >= H or c >= W:
      return False

  return True


# 블록을 놓는 함수
def putCover(H, W, board, nextR, nextC, i):
  positon = L(nextR, nextC, i)
  
  for pos in positon:
    r,c = pos
    if not canPutBlock(r,c):
      return False
    
    if not board[r][c]:
      return False


  for pos in positon:
    r,c = pos
    board[r][c] = False
  
  return True


# 블록을 제거하는 함수
def removeCover(H, W, board, nextR, nextC, i):
  positon = L(nextR, nextC, i)
  
  for pos in positon:
    r,c = pos
    board[r][c] = True
      
  return True


def solve(H,W, board):
  if countWhiteCell(H,W, board) % 3 != 0:
    return 0
  
  return coverCount(H,W, board, 0,0)


def coverCount(H, W, board, startR, startC):
  nextR, nextC = findNextWhiteCell(H, W, board, startR, startC)
  if nextR == -1:
    return 1
  
  count = 0
      
  for i in range(4):
    if putCover(H, W, board, nextR, nextC, i):
      count += coverCount(H, W, board, nextR, nextC+1) # 오른쪽으로 한 칸씩 이동
      removeCover(H, W, board, nextR, nextC, i)
      
  return count
      

# 확인판 만들기
def makeCheckBoard(H,W, board):
  for r in range(H):
    for c in range(W):
      if board[r][c] == '.':
        board[r][c] = True
      
      else:
        board[r][c] = False
        
  return board
  

T = int(sys.stdin.readline())
for _ in range(T):
  H,W = map(int, sys.stdin.readline().split())
  board = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
  board = makeCheckBoard(H,W, board)
  count = solve(H, W, board)
  print(count)
