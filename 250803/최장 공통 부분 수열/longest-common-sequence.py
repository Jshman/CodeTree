A = input()
B = input()

dp = [[0] * (len(A)) for _ in range(len(B)+1)]

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] != B[j]:
            dp[j][i] = max(dp[j][i], dp[j-1][i], dp[j][i-1])
        else:
            dp[j][i] = dp[j-1][i-1] + 1
print(max(dp[len(B) - 1]))