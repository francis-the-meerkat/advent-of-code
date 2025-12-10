a, p = [b.split() for b in open("puzzle1.txt").read().splitlines()], 0

for b in a:
    goal, n = int("".join("1" if c == "#" else "0" for c in b[0][1:-1]), 2), len(b[0][1:-1])
    bts = [int("".join("1" if str(i) in x[1:-1].split(",") else "0" for i in range(n)), 2) for x in b[1:-1]]
    
    queue, com = [(0, 0)], set([0])
    
    while queue:
        stat, tog = queue.pop(0)
        if stat == goal:
            p += tog
            break
        for bt in bts:
            new_stat = stat ^ bt
            if new_stat not in com:
                com.add(new_stat)
                queue.append((new_stat, tog + 1))

print(p)
