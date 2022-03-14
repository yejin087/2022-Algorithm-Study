# n : 마을 수
# c : 트럭 용량
# m : 보내는 박스 개수 정보
n, c = map(int, input().split())
m = int(input())
arr = [list(map(int, input().split())) for i in range(m)]
arr = sorted(arr, key=lambda arr: arr[1])
answer = 0

val = [c]*(n+1)

for s, r, b in arr:
    min_box = min(min(val[s:r], c), b)
    for i in range(s, r):
        val[i] -= min_box
    answer += min_box
print(answer)
