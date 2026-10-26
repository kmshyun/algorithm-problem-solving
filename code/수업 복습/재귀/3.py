import json
def s(i, t):
    if isinstance(i, int):
        return i == t
    for it in i:
        if s(it, t):
            return True
    return False

data = json.loads(input())
target = int(input())
print(s(data, target))