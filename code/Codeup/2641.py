n = int(input())
ans = 0

def f(s, c):
    global ans
    if s == n:
        ans += 1
        return
    if s > n:
        return
    
    for i in (1, 2, 3):
        if i == 3 and c > 0:
            continue
        nc = 2 if i == 3 else max(0, c - 1)
        f(s + i, nc)

f(0, 0)
print(ans)