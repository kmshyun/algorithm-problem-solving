import heapq
import sys

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
prev = {node: None for node in g}

pq = []
heapq.heappush(pq, (0, s))

while pq:
    d, cur = heapq.heappop(pq)

    if d > dist[cur]:
        continue

    for nxt, weight in g.get(cur, []):
        cost = d + weight
        if cost < dist.get(nxt, INF):
            dist[nxt] = cost
            prev[nxt] = cur
            heapq.heappush(pq, (cost, nxt))

ans = dist.get(t, INF)

if ans == INF:
    print(-1)
else:
    path = []
    curr_node = t

    while curr_node is not None:
        path.append(curr_node)
        curr_node = prev.get(curr_node)

    path.reverse()

    print(ans)
    for i in path:
        print(i)