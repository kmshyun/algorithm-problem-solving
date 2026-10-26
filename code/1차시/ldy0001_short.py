n, l = int(input()), [*map(int, input().split())]
T = lambda i: f"{13 + i // 12}:{i % 12 * 5:02d}"
m = max(l)
A = [i for i, x in enumerate(l) if x >= 1000]
print(round(sum(l) / n, 1))
print(m)
print(T(n - 1 - l[::-1].index(m)))
print(len(A))
print(*(T(i) for i in A) if A else "NONE")
print(any(x >= 1300 for x in l) or sum(1000 <= x < 1300 for x in l) >= 3)