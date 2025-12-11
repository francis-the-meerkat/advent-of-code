a = [b.replace(":", "").split() for b in open("puzzle1.txt").read().splitlines()]
goal, p = a[[b[0] for b in a].index("you")][1:], 0

while goal:
    i = goal.pop(0)
    if i == "out": p += 1
        
    for b in a:
        if b[0] == i: goal.extend(b[1:])

print(p)
