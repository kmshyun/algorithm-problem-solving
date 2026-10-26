import json

def d(n):
    if isinstance(n, int):
        return 0
    if len(n) == 0:
        return 1
    dep = 0
    for i in n:
        dep = max(dep, d(i))
    return dep + 1

data = json.loads(input())
print(d(data))