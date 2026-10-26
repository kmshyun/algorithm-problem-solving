n = int(input())
s = []
for i in range(n):
    c = input().split()
    if c == ["UNDO"]:
        if s:
            k = s.pop()
            print(k[1])
        else:
            print('EMPTY')
    else:
        id = c[1]
        s.append(c)