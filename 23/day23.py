class day23:
    def __init__(self, cups):
        self.cups = [int(x) for x in list(cups)]
        self.cur = self.cups[0]
        self.mx = max(self.cups)
        self.ln = len(self.cups)
    def doMoves(self, cnt):
        for i in range(cnt):
            print ("#", i+1)
            self.doMove()
    def doMove(self):
        print (self.cups)
        i = self.cups.index(self.cur)
        c = self.cups[i+1:i+4]
        if len(c) < 3 : c.extend(self.cups[:3-len(c)])
        for x in c: self.cups.remove(x)
        dest = self.cur - 1 if self.cur > 1 else self.mx
        while dest in c:
            dest = dest - 1 if dest > 1 else self.mx
        destIn = self.cups.index(dest)+1
        self.cups = self.cups[:destIn] + c + self.cups[destIn:]
        i = self.cups.index(self.cur)
        print (c)
        print (dest, self.cur)
        self.cur = self.cups[i + 1] if self.ln > i + 1 else self.cups[0] 
#task = day23("389125467") #test
task = day23("326519478") #prod

print (task.cups)
print (task.cur)
task.doMoves(100)
#re = "".join(task.cups)
print(task.cups)


