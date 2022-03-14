# arr = list(map(int, input().split()))
# arr.sort()
# for i in range(1, sum(arr)):
#     ls = [j for j in arr if j <= i]
#     sum = 0
#     while ls:
#         n = ls.pop()
#         if i >= sum+n:
#             sum += n
#         if i == n or i == sum:
#             break
#     else:
#         print(i)
#         break

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range(1, sum(arr)+1):
    ls = [j for j in arr if j <= i]
    sum = 0
    while ls:
        num = ls.pop()
        if num+sum == i:
            break
        elif num+sum < i:
            sum += num
    else:
        print(i)
        break
