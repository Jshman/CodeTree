def union(a, b):
    par_a = findd(a)
    par_b = findd(b)

    if par_a != par_b:
        djs[par_b] = par_a
    return

def findd(a):
    if djs[a] != a:
        djs[a] = findd(djs[a])
        return djs[a]
    return a

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

djs = [i for i in range(n+1)]
for x, y in edges:
    union(min(x,y), max(x,y))
for i in range(1, n+1):
    findd(i)

print(djs.count(djs[1]) -1)