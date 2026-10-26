import sys
sys.set_int_max_str_digits(0)
a, b = input().split()
a = list(map(int, a))[::-1]
b = list(map(int, b))[::-1]
s = 0
c = 0
for i in range(max(len(a), len(b))):
    if i < len(a):
        da = a[i]
    else:
        da = 0
    if i < len(b):
        db = b[i]
    else:
        db = 0
    if da + db + c< 10:
        s += (da+db + c) * 10 **i
        c = 0
    else:
        s += (da+db - 10 + c) * 10 ** i
        c = 1

if c == 1:
    s += 1 * (10 ** max(len(a), len(b)))
print(s)