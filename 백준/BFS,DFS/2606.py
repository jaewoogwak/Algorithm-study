# 2606 바이러스
# https://www.acmicpc.net/problem/2606

import sys;
C = int(input());
N = int(input());
graph = dict();

def DFS(graph, start, count = 0):
    visited = [];
    not_visited = [];

    not_visited.append(start);
    while(not_visited):
        node = not_visited.pop();
        if node not in visited:
            visited.append(node);
            # print(node)
            count = count  + 1;
            not_visited.extend(graph[node]);
    return count;

for i in range(N):
    line = list(map(int, input().split()));
    if line[0] not in graph:
        graph[line[0]] = [line[1]];
    else:
        graph[line[0]] += [line[1]];
    if line[1] not in graph:
        graph[line[1]] = [line[0]];
    else:
        graph[line[1]] += [line[0]];
        

print(DFS(graph, 1)-1);
