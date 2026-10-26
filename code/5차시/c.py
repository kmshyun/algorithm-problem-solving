def sum(x):
    if x != 0:
        x += sum(x-1)
    return x

# method 2

def sum(x):
    if x == 1:
        return 1
    return x + sum(x-1)

print(sum(4))
