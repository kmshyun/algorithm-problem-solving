import json
data = json.loads(input())

def TOTAL(x):
    s = 0
    if isinstance(x, int):
        return x
    else:
        for i in x:
            s += TOTAL(i)

        return s

print(TOTAL(data))