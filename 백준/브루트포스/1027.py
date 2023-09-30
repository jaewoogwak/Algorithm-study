import sys


def main():
    N = sys.stdin.readline()

    arr = list(map(int, sys.stdin.readline().split()))
    ans = float("-inf")
    for x1, y1 in enumerate(arr):
        cnt = 0
        d = float("inf")

        # 왼쪽으로
        for x2 in range(x1, -1, -1):
            y2 = arr[x2]
            if x2 == x1:
                continue
            if x2 > x1:
                continue

            if d > (y2-y1) / (x2-x1):
                d = (y2-y1) / (x2-x1)
                cnt += 1
        d = float("-inf")

        # 오른쪽으로
        for x2, y2 in enumerate(arr):
            if x2 == x1:
                continue
            if x2 < x1:
                continue

            if d < (y2-y1) / (x2-x1):
                d = (y2-y1) / (x2-x1)
                cnt += 1

        ans = max(cnt, ans)

    print(ans)


main()
