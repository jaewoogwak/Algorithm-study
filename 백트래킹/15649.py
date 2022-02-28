# 15649 N과 M (1)
# https://www.acmicpc.net/problem/15649

n, m = map(int, input().split());
visited = [False] * (n+1);
s = [];

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)));
        return;
    for i in range(1, n+1):
        if visited[i] == True:
            continue;
        visited[i] = True;
        s.append(i);
        dfs();
        s.pop();
        visited[i] = False;
dfs();
