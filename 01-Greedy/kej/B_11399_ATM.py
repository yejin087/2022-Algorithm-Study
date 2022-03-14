pn = int(input())
pts = sorted(list(map(int, input().split())))
s = sum(sum(pts[0:i+1]) for i in range(pn))
print(s)

input()
c, s = 0, 0
for i in sorted(list(map(int, input().split(" ")))):
    s += i
    c += s
print(c)
