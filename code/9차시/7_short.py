import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

v, e = map(int, input().split())
s, t = map(int, input().split())
g = [[] for _ in range(v + 1)]
rg = [[] for _ in range(v + 1)]

for _ in range(e):
    u, v_node, w = map(int, input().split())
    g[u].append((v_node, w))
    rg[v_node].append((u, w))

def dj(st, gr):
    dist = [INF] * (v + 1)
    dist[st] = 0

    pq = []
    heapq.heappush(pq, (0, st))

    while pq:
        d, cur = heapq.heappop(pq)

        if d > dist[cur]:
            continue

        for nxt, w in gr[cur]:
            if d + w < dist[nxt]:
                dist[nxt] = d + w
                heapq.heappush(pq, (d + w, nxt))

    return dist

go = dj(s, g)
back = dj(s, rg)

times = 0
for k in range(1, v + 1):
    if k != s and go[k] + back[k] <= t:
        times += 1

print(times)

# 단방향 그래프에서 모든 정점을 갔다가 돌아올때의 경로

'''
= s에서 다익스트라 + 그래프 노드를 다 뒤집은 s에서 다익스트라
'''