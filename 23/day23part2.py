class linkedNode:
    def __init__(self,val):
        self.val = val
        self.prv = None
        self.nxt = None
class day23:
    def __init__(self, cups):
        self.dic = {}
        self.cur = None
        lst = None
        for x in cups:
            lnkNode = linkedNode(int(x))
            if self.cur is None: self.cur = lnkNode
            self.dic[int(x)] = lnkNode
            lnkNode.prv = lst
            lst = lnkNode
        self.frst = self.cur
        mx = 1000000
        for x in range(10, mx+1):
            lnkNode = linkedNode(x)
            lnkNode.prv = lst
            self.dic[x] = lnkNode
            lst = lnkNode
        lst.nxt = self.cur
        c = lst
        lst = None
        mx = 0
        while c is not None:
            if c.val > mx: mx = c.val
            if lst is not None:
                c.nxt = lst
            lst = c
            c = c.prv
        self.mx = mx
    def doMoves(self, cnt):
        for i in range(cnt):
            self.doMove()
    def doMove(self):
        c = self.cur.nxt
        c2 = c.nxt
        c3 = c2.nxt
        self.cur.nxt = c3.nxt #atkirpom 3
        dest = self.cur.val - 1 if self.cur.val > 1 else self.mx
        while dest in [c.val,c2.val,c3.val]:
            dest = dest - 1 if dest > 1 else self.mx
        destIn = self.dic[dest]
        tmp = destIn.nxt
        destIn.nxt = c
        c3.nxt = tmp
        self.cur = self.cur.nxt
    def printCups(self):
        cur = self.frst
        lst = [str(cur.val)]
        cur = cur.nxt
        while cur is not self.frst:
            lst.append(str(cur.val))
            cur = cur.nxt
        print(",".join(lst))
task = day23("326519478") #prod
task.doMoves(10000000)
x = task.dic[1]
print(x.val)
x = x.nxt
print(x.val)
y = x.nxt
print(y.val)
print(x.val * y.val)

