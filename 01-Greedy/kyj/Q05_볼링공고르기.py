# n,m = map(int,input().split())
# bowling = list(map(int,input().split()))
# count = 0

# for idx in range(n):
#     for tmp_bowl in bowling[idx+1:]:
#         if bowling[idx] != tmp_bowl:
#             count += 1
# print(count)


n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0

# 1부터 m 까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i]  # 무게가 i인 볼링공의 개수 제외
    result = array[i] * n  # 두 번째로 선택할 수 있는 경우의 수
