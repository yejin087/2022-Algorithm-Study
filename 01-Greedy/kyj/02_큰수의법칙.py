# n,m,k
# n 개의 숫자.
n = 5
m = 8
k = 3
n_list = [2, 4, 5, 4, 6]
answer = 0

# sorted_n = sorted(n_list, reverse=True)
# print(sorted_n)
# for i in range(m):
#     if (i + 1) % (k + 1) == 0:
#         answer += sorted_n[1]
#     else:
#         answer += sorted_n[0]

# print(answer)

sorted_n = sorted(n_list, reverse=True)
print(sorted_n)
for i in range(m):
    if (i + 1) % (k + 1) == 0:
        answer += sorted_n[1]
    else:
        answer += sorted_n[0]

print(answer)
