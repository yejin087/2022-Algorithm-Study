import itertools
arr = list(map(int, input().split()))
c = list(itertools.combinations(arr, 2))
for i in [(i, i) for i in range(1, max(arr)+1)]:
    if i in c:
        c.remove(i)
print(len(c))
