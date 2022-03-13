# n : 거슬러주어야할 돈 총액
# count : 거슬러 줄 수 있는 동전의 최소 개수
def solution(n):
    coin = [500, 100, 50, 10]
    count = 0
    for c in coin:
        count += n//c
        n = n % c
    return count


print(solution(1650))
