import heapq

q = []
n = int(input())

for i in range(n):
    k = int(input())
    if k == 0:
        if q:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,k)
