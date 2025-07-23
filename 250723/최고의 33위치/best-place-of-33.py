n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def any(y, x):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if grid[y+i][x+j]:
                cnt += 1
    return cnt

ans = 0
for i in range(n-2):
    for j in range(n-2):
        ans = max(ans, any(i, j))
print(ans)