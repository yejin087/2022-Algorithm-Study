# bi = list(map(int,input()))
# curr = bi[0]
# cnt_1 = 0
# cnt_0 = 0
# answer = 0

# for next in bi:
#     if curr != next:
#         if next == 0:
#             cnt_1 += 1
#         elif next == 1:
#             cnt_0 += 1


#     curr = next

# if curr == 1:
#     cnt_1 += 1
# else:
#     cnt_0 += 1

# if cnt_0 > cnt_1:
#     answer = cnt_1
# else:
#     answer = cnt_0

# print(answer)


data = input()
cnt_1 = 0  # 전부 1으로 바꾸는 경우
cnt_0 = 0  # 전부 0으로 바꾸는 경우

# ???
# 첫번째 원소에 대해 처리
if data[0] == "1":
    cnt_0 += 1
else:
    cnt_1 += 1

# 두 번쨰 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == "1":
            cnt_0 += 1
        # 다음 수에서 0으로바뀌는 경우
        else:
            cnt_1 += 1

print(min(cnt_0, cnt_1))
