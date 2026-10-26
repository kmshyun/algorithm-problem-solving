from collections import deque
d = deque()
n = int(input())
for i in range(n):
    c = input()
    if "push" in c:
        cmd = c.split(' ')[1]
        if "b" in c:
            d.append(cmd)
        else:
            d.appendleft(cmd)
    else:
        if d:
            if 'p' in c:
                if 'b' in c:
                    print(d.pop())
                else:
                    print(d.popleft())
            else:
                if 'b' in c:
                    print(d[-1])
                else:
                    print(d[0])
        else:
            print(-1)
