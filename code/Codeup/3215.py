import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

v, e = map(int, input().split())
g = {}

for _ in range(e):
    u, v_node, w = input().split()
    w = int(w)

    g.setdefault(u, []).append((v_node, w))
    g.setdefault(v_node, []).append((u, w))

s, t = input().split()

dist = {node: INF for node in g}
dist[s] = 0

pq = []
heapq.heappush(pq, (0, s))

while pq:
    d, cur = heapq.heappop(pq)
    if d > dist[cur]:
        continue

    for i, w in g[cur]:
        if d + w < dist[i]:
            dist[i] = d + w
            heapq.heappush(pq, (d+w, i))

ans = dist.get(t, INF)
print(-1 if ans == INF else ans)