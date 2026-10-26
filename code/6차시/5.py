n, m, k= map(int, input().split())
l = []
r = 0
def f():
    global r
    # base case
    if len(l) == m:
        print(*l)
        r += 1
        return

    for i in range(1, n+1):
        if i not in l:
            if not l and i != k:
                l.append(i)
                f()
                l.pop()
            elif l:
                if abs(l[-1] - i) % 2 == 1:
                    l.append(i)
                    f()
                    l.pop()

    # recursive case

f()
if r == 0:
    print("NONE")