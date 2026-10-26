from collections import deque
n = int(input())
q = deque()
for i in range(n):
    c = input().split()
    if c[0] == 'ENTER':
        q.append(c[1])
    else:
        if q:
            print(q.popleft())
        else:
            print("EMPTY")
