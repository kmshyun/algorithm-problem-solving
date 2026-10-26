import sys

n, k = map(int, input().split())

l = [0] * n
c = 0

def b(idx, s):
    global c
    if s == k:
        c += 1
        return
    
    if idx >= n:
        return

    if idx == 0 or l[idx - 1] == 0:
        l[idx] = 1
        b(idx + 2, s + 1)
        l[idx] = 0
        
    b(idx + 1, s)

b(0, 0)
print(c)