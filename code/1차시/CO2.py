a = list(map(int, input().split()))

total_sum = 0
mx = a[0]
midx = 0

warn = 0
widx = []

er = 0
eridx = []

vent = False

for idx, val in enumerate(a):
    total_sum += val

    if 1000 <= val < 1300:
        warn += 1
        widx.append(idx)
    elif val >= 1300:
        er += 1
        eridx.append(idx)

    if val >= mx:
        mx = val
        midx = idx

if warn >= 3 or er >= 1:
    vent = True

avg = total_sum / len(a)

print(f"평균: {avg:.2f}")
print(f"최댓값: {mx} (인덱스: {midx})")
print(f"경고 횟수(1000~1299): {warn}회, 위치: {widx}")
print(f"위험 횟수(1300 이상): {er}회, 위치: {eridx}")
print(f"환기 필요 여부: {vent}")