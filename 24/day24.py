class day24:
    def __init__(self, fName):
        lns = open(fName).read().replace("nw", "n").replace("se", "s").splitlines()
        tiles = {}
        for ln in lns:
            y = 0
            x = 0
            for ch in ln:
                if ch == "n":
                    y -= 1
                elif ch == "e":
                    x += 1
                elif ch == "s":
                    y += 1
                elif ch == "w":
                    x -= 1
            coord = str(y) + "," + str(x)
            if coord in tiles:
                tiles[coord] = 1 if tiles[coord] == 2 else 2
            else:
                tiles[coord] = 2 # black
        for ii in range(100):
            newWhites = []
            for t in tiles:
                cur = tiles[t]
                coords = [int(x) for x in t.split(",")]
                c1 = str(coords[0] - 1) + "," + str(coords[1]) #nw
                c2 = str(coords[0] - 1) + "," + str(coords[1]+1) #ne
                c3 = str(coords[0]) + "," + str(coords[1]+1) #e
                c4 = str(coords[0] + 1) + "," + str(coords[1]) #se
                c5 = str(coords[0] + 1) + "," + str(coords[1]-1) #sw
                c6 = str(coords[0]) + "," + str(coords[1]-1) #w
                if c1 not in tiles: newWhites.append(c1)
                if c2 not in tiles: newWhites.append(c2)
                if c3 not in tiles: newWhites.append(c3)
                if c4 not in tiles: newWhites.append(c4)
                if c5 not in tiles: newWhites.append(c5)
                if c6 not in tiles: newWhites.append(c6)
            for nw in newWhites:
                tiles[nw] = 1
            toChange = []
            for t in tiles:
                cur = tiles[t]
                coords = [int(x) for x in t.split(",")]
                c1 = str(coords[0] - 1) + "," + str(coords[1]) #nw
                c2 = str(coords[0] - 1) + "," + str(coords[1]+1) #ne
                c3 = str(coords[0]) + "," + str(coords[1]+1) #e
                c4 = str(coords[0] + 1) + "," + str(coords[1]) #se
                c5 = str(coords[0] + 1) + "," + str(coords[1]-1) #sw
                c6 = str(coords[0]) + "," + str(coords[1]-1) #w
                neigh = [
                    1 if c1 not in tiles else tiles[c1],
                    1 if c2 not in tiles else tiles[c2],
                    1 if c3 not in tiles else tiles[c3],
                    1 if c4 not in tiles else tiles[c4],
                    1 if c5 not in tiles else tiles[c5],
                    1 if c6 not in tiles else tiles[c6],
                ]
                blCnt = 0
                for n in neigh:
                    if n == 2:
                        blCnt += 1
                if cur == 2:
                    if blCnt == 0 or blCnt > 2:
                        toChange.append([t, 1])
                else:
                    if blCnt == 2:
                        toChange.append([t, 2])
            for chng in toChange:
                tiles[chng[0]] = chng[1]
        cnt = 0
        for t in tiles:
            if tiles[t] == 2:
                cnt += 1
        print (cnt)
task = day24("input.txt")
