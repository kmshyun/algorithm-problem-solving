import heapq
v, e = map(int, input().split())
g = {}
INF = float('inf')

for _ in range(e):
    u, v_node, w = input().split()
    w = int(w)

    if u not in g:
        g[u] = []
    if v_node not in g:
        g[v_node] = []

    g[u].append((v_node, w))
    g[v_node].append((u, w))

s,t = input().split()
dist = {node: INF for node in g}
pq = [(0, s)]

while pq:
    d, c = heapq.heappop(pq)
    if d > dist[c]:
        continue
    for nxt, w in g[c]:
        if w + d < dist[nxt]:
            dist[nxt] = d + w
            heapq.heappush(pq, (d+w, nxt))

ans = dist.get(t, INF)
print(-1 if ans == INF else ans)