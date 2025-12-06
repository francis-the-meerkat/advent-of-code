a = open("puzzle1.txt").read().splitlines()
a = list(zip(*[b for b in a]))
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
        if m:
            r = n if not r else r * n
        else:
            r += n

p += r; print(p)
