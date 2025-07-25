n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def sol(idxs=set(), result=0, depth=0, grid=grid):
    if depth == len(grid):
        return result
    ans = 0
    for i in range(len(grid)):
        if i in idxs:
            continue
        idxs.add(i)
        tmp = sol(idxs, result+grid[depth][i], depth+1)
        idxs.remove(i)
        ans = max(ans, tmp)
    return ans

print(sol())