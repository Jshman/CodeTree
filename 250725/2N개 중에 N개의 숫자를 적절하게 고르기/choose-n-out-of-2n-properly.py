n = int(input())
num = list(map(int, input().split()))

num.sort()
rev_num = reverse(num)

print(num)
print(rev_num)