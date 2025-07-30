N, M = map(int, input().split())
coins = list(map(int, input().split()))
# coins.sort()

dp = [0] * (M+1)
for coin in coins:
    if coin < len(dp):
        dp[coin] += 1

for i in range(1, len(dp)):
    if dp[i] > 0:
        for coin in coins:
            if i + coin < len(dp):
                dp[i+coin] = max(dp[coin], dp[i] + 1)
print(dp[-1] if dp[-1] > 0 else -1)