def solution(triangle):
    n = len(triangle)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    dp[0][0] = triangle[0][0]
    
    dy = [1,1]
    dx = [0,1]
    
    for i in range(n - 1):
        for j in range(i + 1):
            for k in range(2):
                nextY = i + dy[k]
                nextX = j + dx[k]
                dp[nextY][nextX] = max(dp[nextY][nextX], dp[i][j] + triangle[nextY][nextX])
                
    answer = max(dp[n-1])
    return answer
