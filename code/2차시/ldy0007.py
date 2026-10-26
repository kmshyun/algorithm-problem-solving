n, m = map(int, input().split())
s = set(input().split())
l = input().split()

c = {}
o = []

for x in l:
    if x in s:
        if x not in c:
            c[x] = 0
            o.append(x)
        c[x] += 1

if not c:
    print("NONE", 0)
else:
    mx = max(c.values())
    for x in o:
        if c[x] == mx:
            print(x, mx)
            break