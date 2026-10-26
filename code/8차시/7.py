from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 100000
dist = [-1] * (MAX + 1)

q = deque([N])
dist[N] = 0

while q:
    curr = q.popleft()

    # 동생의 위치에 도달하면 최단 시간 출력 후 종료
    if curr == K:
        print(dist[curr])
        break

    # 1초 뒤 이동할 수 있는 3가지 위치 확인
    for nxt in (curr - 1, curr + 1, curr * 2):
        if 0 <= nxt <= MAX and dist[nxt] == -1:
            dist[nxt] = dist[curr] + 1
            q.append(nxt)