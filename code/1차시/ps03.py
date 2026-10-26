n = int(input())
l = list(map(int, input().split()))
m = []
k = []
v = False
w = 0

for i in range(len(l)):
    if l[i] >= 1300:
        v = True
        m.append(i)
    elif 1300 >= l[i] >= 1000:
        w += 1
        m.append(i)

    if w >= 3:
        v = True


for i in m:
    h = 13 + (5 * i)//60
    min = str((5 * i)%60)
    if len(min) <= 1:
        min = '0'+ min
    k.append(f"{h}:{min}")

print("NONE" if not m else ' '.join(k))
print(v)
