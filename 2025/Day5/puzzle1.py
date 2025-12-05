a,b = open("puzzle1.txt").read().split('\n\n')
a = [list(map(int, e.split('-'))) for e in a.splitlines()]
b = [int(e) for e in b.splitlines()]
s = set()

for c in a:
    for d in b:
        if int(c[0]) <= int(d) <= int(c[1]):
            s.add(d)


p = len(s)
    
print(p)
