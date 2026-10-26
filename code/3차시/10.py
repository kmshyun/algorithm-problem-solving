from collections import deque
a, b = map(int, input().split())
l = input().split()
q = deque()

for i in l:
    q.append(i)
for i in range(b):
    c = input().split()
    if c[0] == 'LEFT':
        if q:
            k = q.popleft()
            q.append(k)  
    elif c[0] == 'RIGHT':
        if q:
            k = q.pop()
            q.appendleft(k)  

    else:
        print(q.popleft() if q else "EMPTY")
        