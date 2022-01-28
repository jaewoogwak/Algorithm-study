# 19532 수학은 비대면강의입니다.
# https://www.acmicpc.net/problem/19532

line = list(map(int, input().split()));

a = line[0];
b = line[1];
c = line[2];
d = line[3];
e = line[4];
f = line[5];
x =0;
y =0;
if a == 0 or b == 0 or c == 0 or d == 0 or e == 0 or f == 0:
    if a == 0 and b== 0 and d == 0 and e == 0:
        x = 0;
        y = 0;
    elif a == 0 and d == 0:
        if b!=0:
            y = c/b;
        elif e!=0:
            y = f/e;
        x = 0;
    elif a == 0 and d!=0:
        y = c/b;
        x = (f-e*y) / d;
    elif a!=0 and d == 0:
        y =  f/e;
        x = (c-b*y) / a
    elif b == 0 and  e == 0:
        if a !=0:
            x = c /a ;
        elif d!=0:
            x = f/d;
        y = 0;
    elif b == 0 and e !=0:
        x = c/a;
        y = (f-d*x) / e;
    elif b !=0 and e ==0:
        x =  f/d;
        y = (c - a*x) / b;
    x = int(x);
    y = int(y)
    
else:
    y = int((c*d - a*f) / (b*d - a*e));
    x = int((c-b*y) / a);    
      
print(x,y)

    
    
