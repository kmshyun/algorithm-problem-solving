import json
def s(i):
    if isinstance(i, int):
        return 1

    t = 0
    for k in i:
        t += s(k)
    return t

data = json.loads(input())
print(s(data))