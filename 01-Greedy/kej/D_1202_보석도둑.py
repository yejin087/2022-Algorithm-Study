# n: 보석개수, k: 가방 개수
# jewels : 보석 정보 [무게(m), 가격(v)]
# c : 가방에 담을 수 있는 최대 무게
import heapq
import sys

n, k = map(int, input().split())
jews = []
for _ in range(n):
    heapq.heappush(jews, list(map(int, sys.stdin.readline().split())))
print(jews)
# jews = sorted([list(map(int, input().split())) for _ in range(n)])
bags = sorted([int(sys.stdin.readline()) for _ in range(k)])
result = 0

jewsh = []

for bw in bags:
    while jews and jews[0][0] <= bw:
        heapq.heappush(jewsh, -jews[0][1])
        heapq.heappop(jews)

    if jewsh:
        result += -heapq.heappop(jewsh)
    elif not jews:
        break

print(result)
