n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
def move(arr):
    tmp = arr[len(arr)-1]
    for i in range(len(arr)-1, -1, -1):
        arr[i] = arr[i-1]
    arr[0] = -1
    return tmp

for _ in range(t):
    eu = move(u)
    ed = move(d)

    u[0] = ed
    d[0] = eu

print(*u)
print(*d)