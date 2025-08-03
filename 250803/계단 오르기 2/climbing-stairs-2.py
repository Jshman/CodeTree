n = int(input())
coin = list(map(int, input().split()))

dp = [[0]*4 for _ in range(n)]
# i번째 자리까지 더했을 때, 1칸 뛰기는 j번 남았음.
dp[0][1] = coin[0]
dp[1][0] = coin[1]
dp[2][1] = max(coin[0], coin[1]) + coin[2]

for i in range(n):
    for j in range(min(i, 4)):
        # 1칸 뛰기가 j번 남음
        if i%2==0 and j==0: continue
        if i>=1 and j>=1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coin[i])
        if i>=2:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + coin[i])

# for elem in dp:
#     print(elem)

print(max(dp[-1]))