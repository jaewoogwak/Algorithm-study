# 4396 지뢰찾기
# https://www.acmicpc.net/problem/4396
import sys;

N = int(input());
mine = [];
map = []
board = [];

dx = [0, 0, -1, 1, -1, 1, 1, -1];
dy = [-1, 1, 0, 0, -1, 1, -1, 1];
is_clicked_mine = False;

# 지뢰 위치 입력 받기
for i in range(N):
    st = (sys.stdin.readline().split());
    for j in st:
        mine.append(j);
        
# 지뢰판 개방 정보
for i in range(N):
    st = []
    st = (sys.stdin.readline().split());
    for j in st:
        map.append(j);
        
# 지뢰판
for i in range(N):
    st=[];
    for j in range(N):
        st.append('.');
    board.append(st);

for i in range(N):
    for j in range(N):
        count = 0;
        for k in range(8):
            x = i;
            y = j;
            if (0 <= x + dx[k] and x + dx[k] < N) and (0<= y + dy[k] and y +  dy[k] < N):
                # print('arr[{}][{}]의 상하좌우 대각선: arr[{}][{}] {}'.format(x, y, x+dx[k], y+dy[k], mine[(x+dx[k])][(y+dy[k])]))
                if mine[(x+dx[k])][(y+dy[k])] == '*':
                    count +=1;
        if map[i][j] == 'x':
            if mine[i][j] == '*':
                # 지뢰밟음
                is_clicked_mine = True;    
            else: board[i][j] = count;

if is_clicked_mine == True:
    for i in range(N):
        for j in range(N):
            if mine[i][j] == '*':
                board[i][j] = '*';

for i in range(N):
    for j in range(N):
        print(board[i][j], end= '')
    print()
