# 15650 N과 M (2)
# https://www.acmicpc.net/problem/15650

n,m = map(int, input().split());
s = [];
visited = [False] * (n+1);

def dfs():
    if len(s) == m:
        is_ascending = True;
        for i in range(1, len(s)):
            if s[i-1] > s[i]:
                is_ascending = False;
                break;
        if(is_ascending == True):
            print(' '.join(map(str, s)));
            return;
    for i in range(1, n+1):
        if visited[i]:
            continue;
        visited[i] = True;
        s.append(i);
            
        dfs();
        s.pop();
        visited[i] = False;
dfs()
