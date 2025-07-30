N, M = map(int, input().split())
coins = list(map(int, input().split()))

dp = [0] * (M+1)
for coin in coins:
    if coin < len(dp):
        dp[coin] += 1

for i in range(1, len(dp)):
    for coin in coins:
        if i - coin >= 0 and dp[i-coin] > 0:
            dp[i] = max(dp[i], dp[i-coin] + 1)
print(dp[-1] if dp[-1] > 0 else -1)
# print(dp)