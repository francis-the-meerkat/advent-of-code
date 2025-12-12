a = open("puzzle1.txt").read().split("\n\n")
r = [x.split() for x in a.pop().splitlines()]
s = [sum(b.count("#") for b in x.splitlines()[1:]) for x in a]
p = 0

for c in r:
    w, h = map(int, c[0].rstrip(":").replace("x", " ").split())
    endnum = sum(s[n] * int(d) for n, d in enumerate(c[1:]))
    p += endnum <= w * h

print(p)
