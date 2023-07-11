import sys
from collections import deque


def canMove(N, L, R, board, dr, dc):

    for r in range(N):
        for c in range(N):

            for i in range(4):
                nextR = r + dr[i]
                nextC = c + dc[i]

                if nextR >= 0 and nextR < N and nextC >= 0 and nextC < N:
                    gap = abs(board[r][c] - board[nextR][nextC])
                    if gap >= L and gap <= R:
                        return True

    return False


def bfs(N, L, R, board, visited, r, c, dr, dc):

    q = deque()
    united = []

    total = board[r][c]
    q.append((r, c))
    visited[r][c] = True
    united.append((r, c))

    while len(q) > 0:
        curR, curC = q.popleft()

        for i in range(4):
            nextR = curR + dr[i]
            nextC = curC + dc[i]

            if nextR >= 0 and nextR < N and nextC >= 0 and nextC < N:
                if not visited[nextR][nextC]:
                    gap = abs(board[curR][curC] - board[nextR][nextC])
                    if gap >= L and gap <= R:
                        visited[nextR][nextC] = True
                        united.append((nextR, nextC))
                        q.append((nextR, nextC))
                        total += board[nextR][nextC]

    # 연합들 처리
    p = total // len(united)

    for r, c in united:
        board[r][c] = p


def main():
    N, L, R = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cnt = 0

    while True:
        visited = [[False for _ in range(N)] for _ in range(N)]

        if canMove(N, L, R, board, dr, dc):
            for r in range(N):
                for c in range(N):

                    for i in range(4):
                        nextR = r + dr[i]
                        nextC = c + dc[i]

                        if nextR >= 0 and nextR < N and nextC >= 0 and nextC < N:
                            gap = abs(board[r][c] - board[nextR][nextC])
                            if gap >= L and gap <= R and not visited[r][c]:
                                bfs(N, L, R, board, visited, r, c, dr, dc)

            cnt += 1

        else:
            break

    print(cnt)


main()