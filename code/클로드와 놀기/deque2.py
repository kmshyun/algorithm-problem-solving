from collections import deque
n = int(input())
d = deque([i for i in range(1, n+1)])
ans = []
while len(d) > 1:
    a = d.popleft()
    ans.append(a)
    b = d.popleft()
    d.append(b)

ans.append(d[0])
print(*ans)