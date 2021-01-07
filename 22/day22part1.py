class day21:
    def __init__(self, fName):
        ln = open(fName).read().split("\n\n")
        lns = [[int(x) for x in l.splitlines() if x[0:1]!="P"] for l in ln]
        self.lines = lns
    def isWon(self):
        return len(self.lines[1]) == 0 or len(self.lines[0]) == 0
    def whoWon(self):
        return 0 if len(self.lines[1]) == 0 else 1
    def doRound(self):
        p = [self.lines[0].pop(0), self.lines[1].pop(0)]
        win = 0 if p[0] > p[1] else 1
        loo = 0 if win == 1 else 1
        self.lines[win].extend([p[win], p[loo]])
    def getPoints(self, winner):
        winLines = task.lines[winner]
        pts = 0
        for x in range(len(winLines)):
            pts += (len(winLines) - x) * winLines[x]
        return pts            
task = day21("input.txt")
while(task.isWon() == False):
    task.doRound()
winner = task.whoWon()
print(task.getPoints(winner))


