import json
data = input()
k = 0
l = []
for i in data:
    if i == '[':
        k += 1
    elif i == ']':
        k -= 1

    l.append(k)

print(max(l))
