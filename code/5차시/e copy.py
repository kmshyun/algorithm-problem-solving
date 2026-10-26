import json
data = json.loads(input())
k = int(input())

def count(x):
    s = []
    for i in x:
        if isinstance(i, int):
            s.append(i)
        else:
            s += count(i)

    return s