# 3029 경고
# https://www.acmicpc.net/problem/3029

now = (input().split(':'));
now = list(map(int, now))

throw = (input().split(':'));
throw = list(map(int, throw))

count = 0;
if throw == now:
    print("24:00:00")
else :
    ss = (60 - now[2]) + throw[2]
    if ss>60:
        ss = ss % 60;
    elif ss==60:
        ss = ss % 60;
    elif ss<60:
        count = count + 1;
        ss = ss % 60;
    mm = (60 - now[1]) + throw[1] - count;
    count = 0;
    if mm>60:
        mm = mm % 60;
    elif mm == 60:
        mm = mm % 60;
    elif mm <60:
        count = count + 1;
        mm = mm % 60;
    hh = (24- now[0]) + throw[0] - count;
    if hh>=24:
        hh = hh % 24;

    if hh < 10:
        hh = '0' + str(hh);
        if mm < 10:
            mm = '0' + str(mm);
        if ss < 10:
            ss = '0' + str(ss);
            
    print("{}:{}:{}".format(hh, mm ,ss))

    
