import json
def s(i):
    if isinstance(i, int):
        return [i]
    l = []
    for k in i:
        l += s(k)
    return l

data = json.loads(input())
print(s(data))