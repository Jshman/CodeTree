s1 = input()
s2 = input()
N = len(s1)
for i in range(N):
    s1 = s1[-1] + s1[:-1]
    if s1 == s2:
        print(i+1)
        break
else:print(-1)