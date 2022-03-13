n, k = map(int, input().split())
# count = 0
# while True:
#     if(n == 1):
#         break
#     n = n//k if n%k ==0 else n-1
#     count += 1

# print(count)
result = 0
while True:
    target = (n//k)*k
    result += n-target
    n = target

    if n < k:
        break

    n //= k
    result += 1

result += n-1
