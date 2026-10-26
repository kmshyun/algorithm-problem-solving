n = int(input())
s = []
for i in range(n):
    c = input().split()
    if c[0] == "TYPE":
        s.append(c[1])
    else:
        if s:
            s.pop()


print(''.join(s) if s else "EMPTY")