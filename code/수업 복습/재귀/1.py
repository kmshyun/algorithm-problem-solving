def s(n):
    if n == 1:
        return 1
    else:
        return n + s(n-1)

n = int(input())
print(s(n))