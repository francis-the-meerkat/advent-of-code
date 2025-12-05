a, b = open("puzzle1.txt").read().split('\n\n')
a, b = [list(map(int, e.split('-'))) for e in a.splitlines()], [int(e) for e in b.splitlines()]


s = set([d for c in a for d in b if c[0] <= d <= c[1]])
p = len(s)
    
print(p)
