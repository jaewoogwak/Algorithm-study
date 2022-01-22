# 14467 소가 길을 건너간 이유 1
# https://www.acmicpc.net/problem/14467

N = int(input());
cow_and_location = [];
num = [];
for i in range(N):
    observe = list(map(int, input().split()));
    num.append(observe[0]);
    cow_and_location.append([observe[0], observe[1]]);

cow_num = [];
for i in num:
    if i not in cow_num:
        cow_num.append(i);

count = 0;
for num in cow_num:
    # print(num);
    cow = [];
    for j in cow_and_location:
        if num == j[0]:
            cow.append(j);
    # print(cow)
    loc = cow[0][1]
    for j in range(1, len(cow)):
        if loc != cow[j][1]:
            count += 1;
            loc = cow[j][1];
    # print(count)        
    
print(count);
