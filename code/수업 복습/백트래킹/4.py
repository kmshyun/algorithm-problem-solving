n, k, s = map(int, input().split())
c = [i for i in range(1, n+1)]
l = [0]
w = 0
def b(n, k, s):
    global w
    if len(l) == k + 1 and sum(l) == s:
        w += 1
        return
    for i in c:
        if i not in l and l[-1] < i:
            l.append(i)
            b(n, k, s)
            l.pop()

b(n, k, s)
print(w)