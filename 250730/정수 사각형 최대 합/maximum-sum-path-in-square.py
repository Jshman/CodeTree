n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dp[i][j] = grid[i][j] + max(dp[i][j-1], dp[i-1][j])

print(dp[n-1][n-1])