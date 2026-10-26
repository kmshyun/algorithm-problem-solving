n = int(input())
l = list(map(int, input().split()))
s = sum(l)
w = sum(1 for i in l if i >= 1000)

print(round(s / n, 1))

m = l[0]
id = 0
for i, val in enumerate(l):
    if m <= val:
        m = val
        id = i

print(m)
h = 13 + (5 * id) // 60
min = (5 * id) % 60
print(f"{h}:{min:02d}")
print(w)

m = []
k = []
v = False
w = 0

for i, val in enumerate(l):
    if val >= 1300:
        v = True
        m.append(i)
    elif 1000 <= val < 1300:
        w += 1
        m.append(i)
        if w >= 3:
            v = True

for i in m:
    h = 13 + (5 * i) // 60
    min = (5 * i) % 60
    k.append(f"{h}:{min:02d}")

print("NONE" if not m else ' '.join(k))
print(v)