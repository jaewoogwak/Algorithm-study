# 18312 시각
# https://www.acmicpc.net/problem/18312

t = list(map(int, input().split()));
N = t[0]
# print(N);
K = str(t[1])

count = 0;

# i분 j초
for t in range(N+1):
    if t < 10:
        tmp = t;
        hour = "0" + str(tmp);
    else:
        tmp = t;
        hour =str(tmp);
    for i in range(60):
        if i < 10:
            tmp = i;
            min = "0" + str(tmp);
        else:
            tmp = i;
            min =str(tmp);
        for j in range(60):
            if j < 10:
                tmp = j;
                sec = "0" + str(tmp);
            else:
                tmp = j;
                sec = str(tmp);
            time = str(hour) + str(min) + str(sec);
            str(time);
            # print(time)

            if K in time:
                # print(time)
                count+=1;

# print(K)      
print(count);           
