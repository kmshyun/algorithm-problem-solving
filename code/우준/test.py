g = []
for i in range(9):
    s = []
    for j in range(9):
        s.append((i // 3) * 3 + (j // 3) + 1)
    g.append(s)

for i in g:
    print(*i)