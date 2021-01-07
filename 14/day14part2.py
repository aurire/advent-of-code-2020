class day14:
	def __init__(self, fName):
		self.ins = [x.split(" = ") for x in open(fName, "r").read().splitlines()]
		self.mem = {}
	def make(self, mask, xPos):
		ln = len(xPos)
		mx = 2 ** ln
		adrList = []
		for x in range(mx):
			val = "{0:b}".format(x).zfill(ln)
			nVal = mask.copy()
			xx = 0
			for p in range(len(xPos)):
				nVal[xPos[p]]=val[xx]
				xx += 1
			adrList.append(int("".join(nVal),2))
		return adrList
	def run(self):
		mask = "";
		for x in self.ins:
			if (x[0] == "mask"):
				mask = x[1]
			elif(x[0][0:4] == "mem["):
				vl = int(x[1])
				memPlace = int(x[0][4:-1])
				val = "{0:b}".format(memPlace).zfill(len(mask))
				newVal = list(mask)
				posStart = len(mask)-len(val)
				xPos=[]
				for v1 in range(0, len(val)):
					pos = posStart+v1
					if mask[pos] == "0":
						newVal[pos]=val[v1]
					elif mask[pos] == "X":
						xPos.append(pos)
				for yy in self.make(newVal, xPos):
					self.mem[yy] = vl
task = day14("input.txt")
task.run()
sm = 0
for x in task.mem:
	sm += task.mem[x]
print(sm)
