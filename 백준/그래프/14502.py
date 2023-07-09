import sys
from itertools import combinations
from copy import deepcopy


def makeGraph(N, M, g):
    for _ in range(N):
        g.append(list(map(int, sys.stdin.readline().split())))


def bfs(N, M, board, visited, r, c):

    q = []
    q.append((r, c))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while len(q) > 0:
        r, c = q.pop(0)
        visited[r][c] = True


        for i in range(4):
            nextR = r + dr[i]
            nextC = c + dc[i]

            if nextR >= 0 and nextR < N and nextC >= 0 and nextC < M:
                if board[nextR][nextC] == 0:
                    board[nextR][nextC] = 2
                    q.append((nextR, nextC))


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []

    makeGraph(N, M, board)
    temp = deepcopy(board)

    coords = [(r, c) for r in range(N) for c in range(M) if board[r][c] == 0]
    virus = [(r, c) for r in range(N) for c in range(M) if board[r][c] == 2]
    result = list(combinations(coords, 3))
    visited = [[False for _ in range(M)] for _ in range(N)]
    ans = []

    for comb in result:
        for r, c in comb:
            board[r][c] = 1

        # 바이러스가 있는 곳에 대해 bfs 해주기
        for r, c in virus:
            bfs(N, M, board, visited, r, c)

        # 안전 구간 세기
        cnt = 0
        for r in range(N):
            for c in range(M):
                if board[r][c] == 0:
                    cnt += 1

        ans.append(cnt)

        # 맵 다시 복구
        board = deepcopy(temp)

    print(max(ans))


main()
