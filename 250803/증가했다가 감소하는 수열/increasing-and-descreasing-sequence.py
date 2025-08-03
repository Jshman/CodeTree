n = int(input())
points = list(map(int, input().split()))

ans = 1 if points[0] < points[-1] else 0
for i in range(1, n):
    if points[0] < points[i] and points[i] < points[-1]:
        ans *= 3
print(ans)