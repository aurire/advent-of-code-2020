class day25:
    def __init__(self, fName):
        self.lns = [int(x) for x in open(fName).read().splitlines()]
    def getLoopSize(self, target, subj):
        x = 1
        loopSize = 0
        while target != x:
            x *= subj
            x = x % 20201227
            loopSize += 1
        return loopSize
    def transf(self, subj, loops):
        x = 1
        loopSize = 0
        while loopSize != loops:
            x *= subj
            x = x % 20201227
            loopSize += 1
        return x

    def run(self):
        loopSizes = [self.getLoopSize(self.lns[0], 7), self.getLoopSize(self.lns[1], 7)]
        secretKeys = [self.transf(self.lns[0], loopSizes[1]), self.transf(self.lns[1], loopSizes[0])]
        print(loopSizes)
        print(secretKeys)
task = day25("input.txt")
task.run()