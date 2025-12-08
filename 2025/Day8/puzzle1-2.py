import math

a = [tuple(map(int, b.split(","))) for b in open("puzzle1.txt").read().splitlines()]
dist = {}


for b in a:
    for c in a:
        if b > c:
            dist[b,c] = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2 + (b[2] - c[2])**2)

            
def find(x):
    if part[x] != x:
        part[x] = find(part[x])
    return part[x]

def union(x, y):
    xr, yr = find(x), find(y)
    if xr == yr:
        return
    if s[xr] < s[yr]:
        xr, yr = yr, xr
    part[yr] = xr
    s[xr] += s[yr]


part = {x: x for x in a}
s = {x: 1 for x in a}

cords = []
for n, (k, _) in enumerate(sorted(dist.items(), key=lambda x: x[1])):
    cords.append(k)
    if n >= 1000:
        break
    union(k[0], k[1])

circs = {}
for b in a:
    circs[find(b)] = circs.get(find(b), 0) + 1

pl = sorted(circs.values(), reverse=True)[:3]
p1 = 1
for p in pl:
    p1 *= p


part = {}
s = {}

F = []
for v in a:
    part[v] = v
    s[v] = 1

sedges = sorted(dist.items(), key=lambda item: item[1])
for (u, v), w in sedges:
    if find(u) != find(v):
        F.append((u, v))
        union(u, v)


p2 = F[-1][0][0] * F[-1][1][0]

print(p1, "  |  ", p2)
