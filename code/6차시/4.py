n, m, k= map(int, input().split())
l = []
r = 0
def f():
    global r
    if len(l) == m and sum(l) == k:
        r += 1
        return

    for i in range(1, n+1):
        if len(l) == 0 or (i not in l and l[-1] < i):
            l.append(i)

            f()
            l.pop()

    # recursive case

f()
print(r)
