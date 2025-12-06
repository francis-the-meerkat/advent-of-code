a = open("puzzle1.txt").read().splitlines()
a = list(zip(*[l.ljust(max(map(len, a))) for l in a]))
m=p=r = 0

for b in a:
    s = "".join(b)
    if s.strip() == "":
        p += r
        r=m = 0
    if s[-1] == '+': m = 0
    elif s[-1] == '*': m = 1
    n = "".join(c for c in s if c.isdigit())
    if n:
        n = int(n)
        if m == 0:
            r += n
        else:
            r = n if r == 0 else r * n

p += r; print(p)
