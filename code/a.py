def f(s, m):
    count = 0
    s_set = set(s)
    m_set = set(m)
    for i in s_set:
        if i in m_set:
            count += 1

    return count



a = [1,2,3,4]
b = [2,3,4,5]
print(f(a,b))