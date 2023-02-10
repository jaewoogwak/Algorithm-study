# 1212 8진수 2진수
# https://www.acmicpc.net/problem/1212

N = input();
arr = [];
binary = [];
for i in N:
    arr.append(int(i));

for i in arr:
    num = i;
    tmp = [];
    # print('값 : ', num)
    while(1):
        remain = int(num % 2);
        tmp.append(remain);
        num = int(num / 2);
        # print('몫:{} 나머지:{}'.format(num, remain))
        if num < 2 :
            tmp.append(num);
            break;
    if len(tmp) < 3:
        tmp.append(0);
    tmp.reverse();    
    # print(tmp);
    for j in tmp:
        binary.append(j);

# print(binary)
if binary == [0,0,0]:
    print(0);
else:
    count = 0;
    for i in binary:
        if i == 0:
            count += 1;
        else: break;

    for i in range(count):        
        binary.remove(0)

    # print(binary)
    for i in binary:
        print(i, end='');
