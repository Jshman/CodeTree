def min_subsequence_len_dp(arr, m):
    dp = [float('inf')] * (m + 1)
    dp[0] = 0  # 합이 0이 되는 건 원소를 아무것도 안 고른 것

    for num in arr:
        for s in range(m, num - 1, -1):
            if dp[s - num] != float('inf'):
                dp[s] = min(dp[s], dp[s - num] + 1)

    return dp[m] if dp[m] != float('inf') else -1

n, m = map(int, input().split())
A = list(map(int, input().split()))

print(min_subsequence_len_dp(A, m))