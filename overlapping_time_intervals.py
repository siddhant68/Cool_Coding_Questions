intervals = []
for _ in range(int(input())):
    l, r = [int(x) for x in input().split()]
    intervals.append([l, r])

intervals.sort(key=lambda x: x[0])
ans = 1

for i in range(1, len(intervals)):
    j = i-1
    while j >= 0:
        if intervals[j][1] > intervals[i][0]:
            ans += 1
            break

print(ans)