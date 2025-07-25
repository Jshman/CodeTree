n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
def sol(arr=[], nums=num, cnt_zero = 0, limit=n):
    ans = float('inf')
    if len(arr) == limit :
        return abs(sum(arr) - sum(nums))
    
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        arr.append(nums[i])
        nums[i] = 0

        tmp = sol(arr, nums, cnt_zero+1)
        ans = min(ans, tmp)

        nums[i] = arr.pop()
    
    return ans
print(sol())