a = open("puzzle1.txt").read().splitlines()
c, p = 50, 0

for b in a:
    if "R" in b:
        b = int(b[1:])
        c += b
        while c > 99:
            c -= 100
    else:
        b = int(b[1:])
        c -= b
        while c < 0:
            c += 100
    if c == 0:
        p += 1

print(p)
