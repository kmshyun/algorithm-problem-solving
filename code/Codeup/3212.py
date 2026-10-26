import heapq
import sys

input = sys.stdin.readline

v, n = map(int, input().split())
adj = [[] for _ in range(v + 1)]
deg = [0] * (v + 1)

for _ in range(n):
    a, b = map(int, input().split())
    adj[a].append(b)
    deg[b] += 1

pq = [i for i in range(1, v + 1) if deg[i] == 0]
heapq.heapify(pq)
res = []

while pq:
    x = heapq.heappop(pq)
    res.append(x)
    for nx in adj[x]:
        deg[nx] -= 1
        if deg[nx] == 0:
            heapq.heappush(pq, nx)

if len(res) == v:
    for i in res:
        print(i)
else:
    print(-1)