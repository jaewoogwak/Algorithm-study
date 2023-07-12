import sys
import heapq
from collections import deque


def dijkstra(G, s):
    n = len(G)
    X = set()
    A = [float('inf')] * n
    A[s] = 0
    H = [(0, s)]

    while H:
        score, v = heapq.heappop(H)

        if A[v] < score:
            continue

        if v not in X:
            X.add(v)
            A[v] = score
            for w in range(n):
                if G[v][w] > 0 and w not in X:
                    new_score = A[v] + G[v][w]
                    heapq.heappush(H, (new_score, w))

    return A


def main():

    N, E = map(int, sys.stdin.readline().split())
    graph = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]

    for v in range(1, N+1):
        graph[v][v] = 0

    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u][v] = w
        graph[v][u] = w

    v1, v2 = map(int, sys.stdin.readline().split())

    first = dijkstra(graph, 1)
    second = dijkstra(graph, v1)
    third = dijkstra(graph, v2)

    case1 = first[v1] + second[v2] + third[N]
    case2 = first[v2] + third[v1] + second[N]

    ans = min(case1, case2)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)


main()
