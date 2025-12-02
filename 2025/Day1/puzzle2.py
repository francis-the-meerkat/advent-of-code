a = open("puzzle1.txt").read().splitlines()
c, p = 50, 0


for b in a:
    if b[0] == "R":
        b = int(b[1:])
        p += (c + b) // 100
        c = (c + b) % 100
        
    else:
        b = int(b[1:])
        p += abs((c - b) // 100) - (c == 0)
        c = (c - b) % 100
        p += (c == 0)

                
print(p)
