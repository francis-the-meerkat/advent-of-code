a, p1 = [list(b) for b in open("puzzle1.txt").read().splitlines()], 0
i = {(0, a[0].index("S")) : 1}

while True:
    i2 = {}
    for (r,c), n in i.items():
        if r+1 < len(a) and a[r+1][c] == "^":
            p1 += 1
            if c - 1 >= 0:
                i2[(r + 1, c - 1)] = i2.get((r + 1, c - 1), 0) + n
            if c + 1 < len(a[0]):
                i2[(r + 1, c + 1)] = i2.get((r + 1, c + 1), 0) + n

        elif r+1 < len(a):
            i2[(r + 1, c)] = i2.get((r + 1, c), 0) + n
    if not i2:
        break
    i = i2

p2 = sum(i.values())
print(p1,"\n",p2)
