a = [list(b) for b in open("puzzle1.txt").read().splitlines()]


def s():
    b = []    
    for x in range(len(a)):
        for y in range(len(a[0])):
            if a[x][y] == "@":
                c = 0
                for z in [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]:
                    if 0 <= x+z[0] < len(a) and 0 <= y+z[1] < len(a[0]) and a[x+z[0]][y+z[1]] == "@":
                        c += 1
                
                if c < 4:
                    b.append((x,y))
    return(b)


p1 = 0
for x,y in s():
    p1+=1

p2, d = 0, 1
while d:
    d=0
    for x,y in s():
        a[x][y]='x'; p2+=1; d+=1

        
print(p1, "  |  ", p2)
