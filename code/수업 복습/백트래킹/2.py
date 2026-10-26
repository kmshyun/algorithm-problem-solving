n, k = map(int, input().split())
c = [i for i in range(1, n+1)]
l = []
def b(n, k):
    if len(l) == k:
        print(*l)
        return
    for i in c:
        if i not in l:
            l.append(i)
            b(n, k)
            l.pop()

b(n, k)