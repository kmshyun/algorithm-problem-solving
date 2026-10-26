n, k = map(int, input().split())
c = [i for i in range(1, n+1)]
l = [0]
def b(n, k):
    if len(l) == k + 1:
        print(*l[1:])
        return
    for i in c:
        if i not in l and l[-1] < i:
            l.append(i)
            b(n, k)
            l.pop()

b(n, k)