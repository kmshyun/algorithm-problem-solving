import json
data = json.loads(input())

def count(x):
    s = []
    for i in x:
        if isinstance(i, int):
            s.append(i)
        else:
            s += count(i)

    return s

if isinstance(data, int):
    print(data)
else:
    if count(data):
        print(*count(data))
    else:
        print("EMPTY")