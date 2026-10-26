import heapq
a = [(2,1), (3,2)]
heapq.heappush(a, (-10,2))
print(heapq.heappop(a))