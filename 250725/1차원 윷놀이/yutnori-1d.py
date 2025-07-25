n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
board = [0] * m
board[0] = k

def sol(now=0, board=board, nums=nums, depth=0, pieces=k):
    if depth == len(nums):
        score = board[-1]
        return score
    # print(board)
    ans = 0
    # nums에 대해 반복하는 것임
    for i in range(now, len(nums)):
        # 
        for j in range(len(board)):
            if board[j] == 0:
                continue
            board[j] -= 1
            board[min(j + nums[i], len(board)-1)] += 1

            tmp = sol(now+1, board, nums, depth+1)

            board[j] += 1
            board[min(j + nums[i], len(board)-1)] -= 1

            ans = max(ans, tmp)

    return ans

print(sol())