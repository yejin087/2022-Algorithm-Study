def solution(arr):
    arr.sort()
    count = 0
    while arr:
        max = arr[-1]
        arr = arr[0:-max]
        count += 1
    return count


print(solution([2, 3, 1, 2, 2]))
print(solution([2, 4, 1, 2, 4, 5, 2]))
print(solution([1, 2, 2, 3, 5, 3, 1]))

n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 속한 모험가의 수

for i in data:  # 공포도가 낮은 모험가 순서대로 하나씩 확인하며
    count += 1  # 그룹에 해당 모험가 포함
    if count >= i:  # 현재 그룹에 포험된 모험가 수가 현재 공포도 이상이라면 그룹 결성
        result += 1  # 총 그룹 수 증가
        count = 0
print(result)
