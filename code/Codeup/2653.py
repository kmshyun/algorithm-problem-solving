n = int(input())
k = []
c = 0
def b():
    global c
    if len(k) == n:
        c += 1
        return
    for i in [1,0]:
        if not k:
            k.append(i)
            b()
            k.pop()
        else:
            if i == 0 and k[-1] != 0:
                k.append(i)
                b()
                k.pop()
            elif i == 1:
                k.append(i)
                b()
                k.pop()

b()
print(c)