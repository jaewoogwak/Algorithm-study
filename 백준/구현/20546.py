# 20546 기적의 매매법
# https://www.acmicpc.net/problem/20546

money = int(input());
stock = list(map(int, input().split()));

def BNP(money, stock):
    balance = money; # 잔고
    n = 0; # 보유 주식 수
    for i in stock:
        if balance >= i:
            buy = int(balance / i);
            n = int(n + buy);
            balance = balance - (i * buy)        
    total = balance + stock[-1]*n;
    return total;
    # print('BNP total : {}'.format(total))    

def TIMING(money, stock: list):
    balance = money; # 잔고
    n = 0; # 보유 주식 수
    up = 0;
    down = 0;
    
    prev = stock[0];
    for i in stock:
        if prev < i:
            up += 1;
            down = 0;
        elif prev > i:
            down += 1;
            up = 0;
        if(balance >= i):
            if down >= 3:
                # 전량매수
                buy = int(balance / i);
                n = int(n + buy);
                balance = balance - (i * buy);
                # print("전량 매수:{}개 잔고:{}".format(n, balance))
        if n > 0:
            if up >= 3:
                # 전량매도
                balance = balance + (i * n);
                # print("전량 매도:{}개 잔고:{}".format(n, balance))
                n = 0;
        # print('up :{} down:{}'.format(up, down))
        prev = i
            
    total = balance + stock[-1]*n;
    return total;
    # print('TIMING total : {}'.format(total))           
    
bnp = BNP(money, stock);
timing = TIMING(money, stock);

if bnp > timing: print("BNP");
elif bnp < timing : print("TIMING");
elif bnp == timing : print("SAMESAME")
