# def solution(ft, k):
#     fs = list([[i+1, ft[i]] for i in range(len(ft))])
#     idx = 0
#     for t in range(k):
#         idx = t % len(fs)

#         if fs[idx][1] <= 0:
#             idx = (idx+1) % len(fs)
#         fs[idx][1] -= 1
#         print('{}: idx={}'.format(fs, idx))
#     else:
#         idx = (idx+1) % len(fs) if fs[idx][1] <= 0 else idx
#     return idx+1


# print(solution([3, 1, 2], 5))
# print(solution([3, 5, 1], 7))

import heapq


# k: 총 시간
def solution(ft, k):
    heap = []
    wasted = 0  # 먹기 위해 사용된 시간
    flen = len(ft)

    if k >= sum(ft):
        return -1
    for idx, val in enumerate(ft):
        heapq.heappush(heap, (val, idx+1))

    while (heap[0][0]-wasted) * flen <= k:
        del_ftime = heapq.heappop(heap)[0]
        k -= (del_ftime-wasted) * flen
        wasted += (del_ftime-wasted)
        flen -= 1

    result = sorted(heap, key=lambda x: x[1])
    return result[k % flen][1]


print(solution([3, 1, 2], 5))
print(solution([3, 5, 1], 7))
