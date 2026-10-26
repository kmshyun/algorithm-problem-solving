n, m = map(int, input().split())
l = []

def f():
    # base case
    if len(l) == m:
        print(*l)
        return

    for i in range(1, n+1):
        if i not in l:
            l.append(i)

            f()
            l.pop()

    # recursive case

f()


'''
1 2
1 3
2 1
2 3
'''