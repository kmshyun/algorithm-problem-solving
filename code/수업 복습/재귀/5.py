def is_pelindrome(t, l, r):
    if l >= r:
        return True
    if t[l] != t[r]:
        return False
    return is_pelindrome(t, l+1, r-1)

text = input().strip()
print(is_pelindrome(text, 0, len(text)-1))