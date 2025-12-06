a = [b.split() for b in open("puzzle1.txt").read().splitlines() if b.strip()]
a, p = zip(*a), 0


for b in a:
    x = 0
    for c in b[:-1]:
        if b[-1] == "+": x += int(c)
        elif b[-1] == "*":
            if x == 0: x = int(c)
            else: x *= int(c)
    p += x

print(p)
