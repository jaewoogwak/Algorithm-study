# 수들의 합 5
# https://www.acmicpc.net/problem/2018

N = int(input());
start=0;
end=0;
summary=0;
count=0;

for start in range(N):
    while summary < N and end < N:
        summary = summary + (end +1);
        end = end + 1;
    if summary == N:
        count+=1;
    summary = summary - (start+1);

print(count);
