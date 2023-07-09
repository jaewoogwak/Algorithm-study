import sys
import collections


maximum = 0


def getSize(visited: list):

    size = 0
    for v in visited:
        if v:
            size += 1

    return size


def dfs(R, C, board, visited: list, currR, currC, cnt):
    global maximum
    maximum = max(maximum, cnt)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        nextR = currR + dr[i]
        nextC = currC + dc[i]

        if nextR >= 0 and nextR < R and nextC >= 0 and nextC < C:
            idx = ord(board[nextR][nextC])-65
            if not visited[idx]:
                visited[idx] = True
                dfs(R, C, board, visited, nextR, nextC, cnt+1)
                visited[idx] = False


def main():

    R, C = map(int, sys.stdin.readline().split())

    board = [list(map(str, sys.stdin.readline().rstrip()))
             for _ in range(R)]

    visited = [False] * 27
    visited[ord(board[0][0])-65] = True

    dfs(R, C, board, visited, 0, 0, 1)

    global maximum
    print(maximum)


main()
