n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()

cnt = 0
selected_end = -1
for x1, x2 in lines:
    if selected_end <= x1:
        selected_end = x2
        cnt += 1
print(cnt)
