n, m, k = map(int, input().split())
l = []
r = 0
def b(n, m, k):
    global r
    if len(l) == m:
        print(*l)
        r += 1
        return
    for i in range(1, n+1):
        if (not l and i != k) or (l and l[-1]%2 != i%2 and i not in l):
            l.append(i)
            b(n, m, k)
            l.pop()

b(n, m, k)
if r == 0:
    print("NONE")