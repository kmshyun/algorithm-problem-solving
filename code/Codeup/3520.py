import sys
input = sys.stdin.readline

n = int(input())
l = []
s = 0

vc = [False] * n
vd = [False] * (2 * n)
vdd = [False] * (2 * n)

def b():
    global s
    curr_len = len(l)
    if curr_len == n:
        if s < 3:
            k = [i + 1 for i in l]
            s += 1
            print(*k)
        return 1
    
    c = 0
    for r in range(n):
        if not con(r, curr_len):
            continue
        l.append(r)
        vc[r] = True
        vd[curr_len - r + n] = True
        vdd[curr_len + r] = True
        c += b()

        l.pop()
        vc[r] = False
        vd[curr_len - r + n] = False
        vdd[curr_len + r] = False

    return c

def con(r, curr_len):
    if vc[r]:
        return False
    if vd[curr_len - r + n]:
        return False
    if vdd[curr_len + r]:
        return False
    return True

print(b())