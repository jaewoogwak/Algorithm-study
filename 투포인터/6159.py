# 6159 코스튬 파티
# https://www.acmicpc.net/problem/6159

N, S = list(map(int, input().split()));
cow = [];

for i in range(N):
    c = int(input())
    cow.append(c);

cow = sorted(cow);

start = 0;
end = 1;
pair_sum = 0;
count = 0;

t = cow[0] + cow[1]
# print(cow);
for start in range(len(cow)):
    if start > S:
        break;
    end = start + 1;
    while end<N and t <= S and start != end:
        pair_sum = cow[start] + cow[end];
        if pair_sum <= S:
            count = count + 1;    
            # print(cow[start], cow[end], 's :',start, "e: ", end)
        end = end +1;

print(count)
