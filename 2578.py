# 2578 빙고
# https://www.acmicpc.net/problem/2578

board = [];
number = [];
bingo_counter = 0;
count = 0;

def isBingo(bingo_counter):
    # 가로줄 검사
    for i in range(5):
        if board[i][0] == 0 and board[i][1] == 0 and board[i][2] == 0 and board[i][3] == 0 and board[i][4] == 0:
            bingo_counter +=1;
    # 세로줄 검사
    for i in range(5):
        if board[0][i] == 0 and board[1][i] == 0 and board[2][i] == 0 and board[3][i] == 0 and board[4][i] == 0:
                bingo_counter +=1;
    # 대각선 검사
    if board[0][0] == 0 and board[1][1] == 0 and board[2][2] == 0 and board[3][3] == 0 and board[4][4] == 0:
        bingo_counter +=1;
    if board[0][4] == 0 and board[1][3] == 0 and board[2][2] == 0 and board[3][1] == 0 and board[4][0] == 0:              
        bingo_counter +=1;
    
    return bingo_counter;           
      
# 빙고판 생성
for i in range(5):
    line = list(map(int, input().split()));
    board.append(line);

# 사회자가 숫자 부르기
for i in range(5):
    num = list(map(int, input().split()));
    for j in num:
        number.append(j);
        
for num in number:
    count +=1;
    for line in board:
        for space in line:
            if space == num:
                board[board.index(line)][line.index(space)] = 0;
                n = isBingo(bingo_counter);
                if n >= 3:
                    print(count);
                    exit(0);
