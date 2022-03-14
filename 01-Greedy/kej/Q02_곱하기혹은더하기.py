def solution(s):
    arr = list(map(int, s))
    answer = arr.pop(0)
    while arr:
        num = arr.pop(0)
        # answer = max(answer+num, answer*num)
        if answer > 1 and num > 1:
            answer *= num
        else:
            answer += num
    return answer


print(solution('02984'))  # 576


data = input()
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
