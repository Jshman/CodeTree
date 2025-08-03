A = input()
B = input()

dp = [[""] * (len(A)+1) for _ in range(len(B)+1)]
for i in range(len(A)):
    dp[0][i+1] = A[i]
for j in range(len(B)):
    dp[j+1][0] = B[j]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        a = A[i-1]
        b = B[j-1]

        if a != b:
            if j-1>0 and len(dp[j][i]) < len(dp[j-1][i]):
                dp[j][i] = dp[j-1][i]
            if i-1>0 and len(dp[j][i]) < len(dp[j][i-1]):
                dp[j][i] = dp[j][i-1]
        else:
            if j -1 > 0 and i-1>0:
                dp[j][i] = dp[j-1][i-1] + b
            else:
                dp[j][i] = b

ans = ''
for arr in dp:
    for elem in arr:
        if len(ans) < len(elem):
            ans = elem
print(ans)