n = list(map(int, input()))
result = 0

# if n[0] == 0 or n[1] == 0:
#        result =  n[0] + n[1]

# for i in n[2:]:
#     if i == 0:
#         result += i
#     else:
#         result *= i


if n[0] == 0 or n[1] == 0:
    result = n[0] + n[1]

for i in n[2:]:
    if i == 0:
        result += i
    else:
        result *= i

print(result)
