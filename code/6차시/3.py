n, m = map(int, input().split())
l = []

def f():
    # base case
    if len(l) == m:
        print(*l)
        return

    for i in range(1, n+1):
        if len(l) == 0 or (i not in l and l[-1] < i):
            l.append(i)

            f()
            l.pop()

    # recursive case

f()

n, m = map(int, input().split())
l = []
def f(s):
    if len(l) == m:
        print(*l)
        return

    for i in range(s, n + 1):
        l.append(i)
        f(i + 1)
        
        l.pop()
f(1)


'''
1 2 3
1 2 4
'''