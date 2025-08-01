n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
# dp[0][0] = grid[0][0]

for i in range(n):
    for j in range(n):
        if 0<=i-1<n and 0<=j-1<n:
            dp[i][j] = min(grid[i][j], max(dp[i-1][j], dp[i][j-1]))
        elif 0<=i-1<n:
            dp[i][j] = min(grid[i][j], dp[i-1][j])
        elif 0<=j-1<n:
            dp[i][j] = min(grid[i][j], dp[i][j-1])
        else:
            dp[i][j] = grid[i][j]

print(dp[n-1][n-1])

