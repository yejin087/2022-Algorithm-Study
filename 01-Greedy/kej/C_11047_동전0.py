n, m = list(map(int, input().split()))
arr = [int(input()) for i in range(n)]
arr.reverse()
answer = 0
for i in arr:
    answer += m//i
    m = m % i
print(answer)
