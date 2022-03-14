def solution(n, m, k, arr):
    answer = 0
    count = 0

    first = sorted(arr)[-1]
    second = sorted(arr)[-2]

    count = (m//(k+1))*k
    count += m % (k+1)

    answer += first*count
    answer += second*(m-count)

    return answer


print(solution(5, 8, 3, [2, 4, 5, 4, 6]))  # 46
print(solution(5, 7, 2, [3, 4, 3, 4, 3]))  # 28
