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
        cnt = 0
        for t in tiles:
            if tiles[t] == 2:
                cnt += 1
        print (cnt)
task = day24("input.txt")
