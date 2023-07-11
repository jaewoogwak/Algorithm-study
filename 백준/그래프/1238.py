import sys
import heapq
from collections import deque


def dijkstra(G, s):
    n = len(G)
    X = set()
    A = [float('inf')] * n
    A[s] = 0
    H = [(0, s)]

    # print("H", H, "A", A, "Graph", G)
    while H:
        score, v = heapq.heappop(H)

        if v not in X:
            X.add(v)
            A[v] = score
            for w in range(n):
                if G[v][w] > 0 and w not in X:
                    new_score = A[v] + G[v][w]
                    heapq.heappush(H, (new_score, w))
    return A


def initGraph(graph, N, edge):
    for v in range(N):
        graph.append([0] * N)

    for i in range(0, len(edge)-2, 3):
        graph[edge[i]][edge[i+1]] = edge[i+2]

    # print(graph, edge)


def main():

    N, M, X = map(int, sys.stdin.readline().split())

    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    graph = [[0 for _ in range(0, N+1)] for _ in range(0, N+1)]
    for i in range(0, M):
        s, e, w = edges[i]
        graph[s][e] = w

    shortestBoard = [[0 for _ in range(0, N+1)] for _ in range(0, N+1)]

    for v in range(1, N+1):
        path = dijkstra(graph, v)  # n번(1~N번) 노드에서 v번 노드까지 최단거리

        for p in range(N+1):
            shortestBoard[v][p] = path[p]

    shortestPath = [0 for _ in range(N+1)]

    for v in range(1, N+1):
        shortestPath[v] = shortestBoard[v][X] + shortestBoard[X][v]

    print(max(shortestPath))


main()
