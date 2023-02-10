# 15652 N과 M (4)
# https://www.acmicpc.net/problem/15652

n,m = map(int, input().split());
s = [];
visited = [False] * (n+1);

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)));
        return;
    for i in range(1, n+1):
        if visited[i]:
            continue;
        # visited[i] = True;

        
        
        if len(s) >= 1:
            if s[-1] > i:
                continue;
            else:
                s.append(i);
        else:
            s.append(i);
        dfs();
        s.pop();
        visited[i] = False;
dfs()
