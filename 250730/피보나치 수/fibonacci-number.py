N = int(input())

fibo = [0, 1, 1]
for i in range(N-2):
    fibo[i%3] = fibo[(i+1)%3] + fibo[(i+2)%3]
print(fibo[N%3])