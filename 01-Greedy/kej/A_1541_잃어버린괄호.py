arr = list(input().split('-'))
arr = [sum(map(int, i.split('+'))) for i in arr]

answer = arr[0]
for idx in range(1, len(arr)):
    answer -= arr[idx]
print(answer)
