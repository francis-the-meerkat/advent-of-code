import re

a, p1, p2 = [e.split('-') for e in open("puzzle1.txt").read().split(",")], 0, 0


for b in a:
    for c in range(int(b[0]), int(b[1])+1):
        if re.search(r'^(\d+)\1{1}$', str(c)):
            p1 += c
        if re.search(r'^(\d+)\1{1,}$', str(c)):
            p2 += c

print(p1, " | ", p2)
