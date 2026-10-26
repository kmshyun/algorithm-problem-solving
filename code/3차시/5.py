l = list(input())
s = []
s.append(l[0])
for i in range(1, len(l)):
    if not s:
        s.append(l[i])
    elif s[-1] != l[i]:
        s.append(l[i])
    else:
        s.pop()
print(''.join(s) if s else "EMPTY")