# N과 M (5)
# https://www.acmicpc.net/problem/15654

n,m = map(int, input().split());
arr = list(map(int, input().split()));
arr.sort();
s = [];
visited = [False] * (n+1);

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)));
        return;
    for i in range(1, n+1):
        if visited[i]:
            continue;
        visited[i] = True;
        s.append(arr[i-1]);
        dfs();
        s.pop();
        visited[i] = False;
dfs();
