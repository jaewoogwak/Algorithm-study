# https://www.acmicpc.net/problem/1260


import sys
from collections import deque


def makeGraph(N, M, g):
    for i in range(1, N+1):
        g[i] = []

    for i in range(M):
        s, e = map(int, sys.stdin.readline().split())
        g[s].append(e)
        g[e].append(s)

    for i in range(1, N+1):
        g[i] = sorted(g[i], reverse=True)


def dfs(N, g, visited: list, start):

    visited.append(start)

    for next in sorted(g[start]):
        if next not in visited:
            dfs(N, g, visited, next)


def dfs2(N, g, visited, start):
    needVisited = [start]

    while len(needVisited) > 0:
        v = needVisited.pop()

        if v not in visited:
            visited.append(v)

            needVisited.extend(g[v])


def bfs(N, g, visited, start):

    q = []
    q.append(start)
    visited.append(start)

    while len(q) > 0:
        v = q.pop(0)

        for next in sorted(g[v]):

            if next not in visited:
                visited.append(next)
                q.append(next)


def main():
    N, M, V = map(int, sys.stdin.readline().split())

    g = {}

    makeGraph(N, M, g)

    visited = []
    dfs(N, g, visited, V)
    print(*visited)

    visited = []
    bfs(N, g, visited, V)
    print(*visited)


main()
