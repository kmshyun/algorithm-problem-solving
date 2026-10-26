n = int(input())

def s(n):
    k = [0] * (n+1)
    k[1] = 1
    if n >= 2:
        k[2] = 2
    if n >= 3:
        k[3] = 4

    for i in range(4, n+1):
        k[i] = k[i-1] + k[i-2] + k[i-3]

    return k[n]

for i in range(n):
    a = int(input())
    print(s(a))