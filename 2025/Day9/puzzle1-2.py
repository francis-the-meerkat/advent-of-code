a = [tuple(map(int, b.split(","))) for b in open("puzzle1.txt").read().splitlines()]
e = list(zip(a, a[1:] + a[:1]))

p1 = p2 = 0

for b in a:
    for c in a:
        x, y = sorted((b[0], c[0])), sorted((b[1], c[1]))
        area = (abs(x[0] - x[1]) + 1) * (abs(y[0] - y[1]) + 1)
        
        p1 = max(p1, area)

        if area > p2:
            if not any(
                (x[0] < ux < x[1] and max(y[0], min(uy, vy)) < min(y[1], max(uy, vy))) or
                (y[0] < uy < y[1] and max(x[0], min(ux, vx)) < min(x[1], max(ux, vx))) for (ux, uy), (vx, vy) in e):

                p2 = area

print(p1, "  |  ", p2)
