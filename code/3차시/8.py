from collections import deque
n = int(input())
q = deque()
for i in range(n):
    c = input().split()
    if c[0] == 'REQUEST':
        q.append(c[1])
    else:
        if q:
            q.popleft()

print(' '.join(q) if q else "EMPTY")
