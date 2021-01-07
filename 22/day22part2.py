import hashlib
class game: #day21
    def __init__(self, lns):
        self.lines = lns
        self.matches = {}
        self.mem = {}
    def isWon(self):
        return len(self.lines[1]) == 0 or len(self.lines[0]) == 0
    def whoWon(self):
        if len(self.lines[1]) != 0 and len(self.lines[0]) != 0: return 0
        return 0 if len(self.lines[1]) == 0 else 1
    def doHash(self, p1, p2):
        uniq = "-".join([str(inte) for inte in p1]) + "|" + "-".join([str(inte) for inte in p2])
        return int(hashlib.md5(uniq.encode()).hexdigest(), 16)
    def doRound(self):
        hsh = self.doHash(self.lines[0], self.lines[1])
        if hsh in self.matches: return 1
        p = [self.lines[0].pop(0), self.lines[1].pop(0)]
        if p[0] <= len(self.lines[0]) and p[1] <= len(self.lines[1]):
            slice1 = self.lines[0][:p[0]]
            slice2 = self.lines[1][:p[1]]
            hsh2 = self.doHash(slice1, slice2)
            if hsh2 in self.mem:
                win = self.mem[hsh2] - 1
            else:
                recurseGame = game([slice1, slice2])
                recurseGame.mem = self.mem
                win = recurseGame.play()
                self.mem[hsh2] = win+1
                self.mem = {**self.mem, **recurseGame.mem}
        else:
            win = 0 if p[0] > p[1] else 1
        loo = 0 if win == 1 else 1
        self.lines[win].extend([p[win], p[loo]])
        self.matches[hsh] = win+1
    def getPoints(self, winner):
        winLines = self.lines[winner]
        pts = 0
        for x in range(len(winLines)):
            pts += (len(winLines) - x) * winLines[x]
        return pts
    def play(self):
        winner = None
        while(self.isWon() == False):
            roundRez = self.doRound()
            if roundRez:
                winner = roundRez - 1
                break
        winner = self.whoWon()
        self.points = self.getPoints(winner)
        return winner
fName = "input.txt"
ln = open(fName).read().split("\n\n")
lns = [[int(x) for x in l.splitlines() if x[0:1] != "P"] for l in ln]
task = game(lns)
task.play()
print(task.points)
