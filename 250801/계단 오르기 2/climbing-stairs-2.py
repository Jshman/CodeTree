n = int(input())
coin = list(map(int, input().split()))

dp = [[0]*4 for _ in range(n)]
# i번째 자리까지 더했을 때, 1칸 뛰기는 j번 남았음.
dp[0][1] = coin[0]
dp[1][0] = coin[1]
dp[2][1] = max(coin[0], coin[1]) + coin[2]

for i in range(1, n):
    for j in range(4):
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coin[i])
        if i-2 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + coin[i])

print(max(dp[n-1]))