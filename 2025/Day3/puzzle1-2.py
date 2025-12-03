a = open("puzzle1.txt").read().splitlines() 

def s(l):
    p = 0
    for b in a:
        c, d = "", 0
        for n, _ in enumerate(range(1, l)):
            c = c + str(max(b[d:-(l-n-1)]))
            d = b.index(max(b[d:-(l-n-1)]), d)+1
        p += int(c + str(max(b[d:])))
    return(p)

print(s(2), "  |  ", s(12))
