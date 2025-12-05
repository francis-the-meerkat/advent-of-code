a = sorted([list(map(int, r.split('-'))) for r in open("puzzle1.txt").read().split('\n\n')[0].splitlines()])

s = [a[0]]

for b, c in a[1:]:
    if b <= s[-1][1] or b == s[-1][1] + 1:
        s[-1][1] = max(s[-1][1], c)
    else:
        s.append([b,c])

p = sum(d[1] - d[0] + 1 for d in s)

print(p)
