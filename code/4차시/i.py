import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))

left = 0
right = n-1
s = 0

while left < right:
    if l[left] + l[right] <= k:
        s += right - left
        left += 1

    else:
        right -= 1

print(s)