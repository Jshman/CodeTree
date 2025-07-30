N, M = map(int, input().split())
coin = list(map(int, input().split()))

dp = [float('inf')] * (M+1)
for c in coin:
    if c <= M:
        dp[c] = 1

for i in range(1, M+1):
    for c in coin:
        if i >= c:
            dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[M])