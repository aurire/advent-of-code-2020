class day11:
	def __init__(self, fName):
		self.step = 0
		self.ins = open(fName, "r").read().splitlines()
		self.ins = [list(x) for x in self.ins]
		self.tmp = []
	def getOccInDirection(self, x, y, px, py):
		zx = x + px
		zy = y + py
		while zy >= 0 and zy < len(self.ins) and zx >= 0 and zx < len(self.ins[0]):
			if self.tmp[zy][zx] == "#":
				return 1
			elif self.tmp[zy][zx] == "L":
				return 0
			zx += px
			zy += py
		return 0
	def getOccupied(self, x, y):
		occupied = 0
		occupied += self.getOccInDirection(x, y, -1, -1)
		occupied += self.getOccInDirection(x, y, -1, 0)
		occupied += self.getOccInDirection(x, y, -1, 1)
		occupied += self.getOccInDirection(x, y, 0, -1)
		occupied += self.getOccInDirection(x, y, 0, 1)
		occupied += self.getOccInDirection(x, y, 1, -1)
		occupied += self.getOccInDirection(x, y, 1, 0)
		occupied += self.getOccInDirection(x, y, 1, 1)
		return occupied
	def rule1(self, x, y):
		if self.tmp[y][x] == "L":
			if self.getOccupied(x, y) == 0:
				self.ins[y][x] = "#"
	def rule2(self, x, y):
		if self.tmp[y][x] == "#":
			occc = self.getOccupied(x, y)
			if occc >= 5:
				self.ins[y][x] = "L"
	def apply(self, rule):
		tmp = []
		for y in range(len(self.ins)):
			tmp2 = []
			for x in range(len(self.ins[0])):
				tmp2.append(self.ins[y][x])
			tmp.append(tmp2)
		self.tmp = tmp
		for y in range(len(self.ins)):
			for x in range(len(self.ins[0])):
				rule(x, y)
		self.step += 1
	def pr(self):
		print("Step: ", self.step)
		for y in range(len(self.ins)):
			print(''.join(self.ins[y]))
	def occ(self):
		sum = 0
		for y in range(len(self.ins)):
			for x in range(len(self.ins[0])):
				if self.ins[y][x] == "#":
					sum += 1
		return sum

task = day11("input.txt")
last = task.occ()
# task.apply(task.rule1)
# task.pr()
# task.apply(task.rule2)
# task.pr()

while True:
	task.apply(task.rule1)
	n = task.occ()
	if last == n:
		break
	last = n
	task.apply(task.rule2)
	n = task.occ()
	if last == n:
		break
	last = n
task.pr()
print("Occupied:", last)
