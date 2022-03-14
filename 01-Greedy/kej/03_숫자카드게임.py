n, m = map(int, input().split())
answer = []

for i in range(n):
    ls = list(map(int, input().split()))
    answer.append(min(ls))

print(max(answer))
