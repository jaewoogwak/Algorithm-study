# 15721 번데기
# https://www.acmicpc.net/problem/15721

A = int(input());
T = int(input());
n = int(input());

count_bbun = 0;
count_deagi = 0;
game = [];
for i in range(100):
    for j in range(2):
        game.append("뻔");
        game.append("데기");
    for k in range(i+2):
        game.append("뻔");
    for k in range(i+2):
        game.append("데기")
# 구호가 '뻔'일 때
if n == 0:        
    for i in range(len(game)):
        if game[i] == '뻔':
            count_bbun += 1;
        if count_bbun == T:
            idx = i;
            break;
    num = idx % A
    print(num)
else:
    for i in range(len(game)):
        if game[i] == '데기':
            count_deagi += 1;
        if count_deagi == T:
            idx = i;
            break;
    num = idx % A
    print(num)
