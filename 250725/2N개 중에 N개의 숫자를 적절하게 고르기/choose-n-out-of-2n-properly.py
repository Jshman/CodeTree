n = int(input())
num = list(map(int, input().split()))
sum_num = sum(num)

# Please write your code here.
def sol(now=0, arr=[], nums=num, limit=n, S=sum_num):
    ans = float('inf')
    if len(arr) == limit :
        return abs(sum(arr)*2 - S)
    
    for i in range(now, len(nums)):
        if nums[i] == 0:
            continue
        arr.append(nums[i])
        nums[i] = 0

        tmp = sol(i+1, arr, nums)
        ans = min(ans, tmp)

        nums[i] = arr.pop()
    
    return ans
print(sol())
