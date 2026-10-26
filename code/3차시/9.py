from collections import deque
a = int(input())
q = deque()
for i in range(a):
    c = input().split()
    if c[0] == "REMOVE_LEFT":
        if q:
            print(q.popleft())
        else:
            print("EMPTY")
    elif c[0] == "REMOVE_RIGHT":
        if q:
            print(q.pop())
        else:
            print("EMPTY")

    elif c[0] == "ADD_LEFT":
        q.appendleft(c[1])
    else:
        q.append(c[1])