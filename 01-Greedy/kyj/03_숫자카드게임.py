# n,m을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
for i in range(n):
    # 한 줄씩 입력 받아 확인
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_val = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_val)

print(result)
