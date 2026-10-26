n, k = map(int, input().split())
l = list(map(int, input().split()))
left = 0
right = n-1
while left < right:
    s = l[left] + l[right]
    if s < k:
        left += 1
    elif s > k:
        right -= 1
    elif s == k:
        break

print(left+1, right+1)


'''

데이터가 오름차순이므로
크면 right -1
작으면 left +1
left <= right 일때까지

'''