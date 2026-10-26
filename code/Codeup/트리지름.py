n = int(input())
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))


def dfs(s, d):
    for i, w in g[s]:
        if distance[i] == -1:
            distance[i] = distance[s] + w
            dfs(i, d + w)

# 1. 1번 노드에서 시작하여 가장 먼 노드 m 탐색
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)
m = distance.index(max(distance))

# 2. 가장 먼 노드 m에서 다시 시작하여 트리의 지름 구하기
distance = [-1] * (n + 1)
distance[m] = 0
dfs(m, 0)  # m에서 출발

print(max(distance))