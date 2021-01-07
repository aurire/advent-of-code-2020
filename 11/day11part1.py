class day11:
	def __init__(self, fName):
		self.step = 0
		self.ins = open(fName, "r").read().splitlines()
		self.ins = [list(x) for x in self.ins]
		self.tmp = []
	def getOccupiedAndEmpty(self, x, y):
		occupied = 0
		empty = 0
		if y > 0:
			if x > 0:
				if self.tmp[y - 1][x - 1] == "#":
					occupied += 1
				elif self.tmp[y - 1][x - 1] == "L":
					empty += 1
			if self.tmp[y - 1][x] == "#":
				occupied += 1
			elif self.tmp[y - 1][x] == "L":
				empty += 1
			if x < len(self.ins[0]) - 1:
				if self.tmp[y - 1][x + 1] == "#":
					occupied += 1
				elif self.tmp[y - 1][x + 1] == "L":
					empty += 1
		if x > 0:
			if self.tmp[y][x - 1] == "#":
				occupied += 1
			elif self.tmp[y][x - 1] == "L":
				empty += 1
		if x < len(self.ins[0]) - 1:
			if self.tmp[y][x + 1] == "#":
				occupied += 1
			elif self.tmp[y][x + 1] == "L":
				empty += 1
		if y < len(self.ins) - 1:
			if x > 0:
				if self.tmp[y + 1][x - 1] == "#":
					occupied += 1
				elif self.tmp[y + 1][x - 1] == "L":
					empty += 1
			if self.tmp[y + 1][x] == "#":
				occupied += 1
			elif self.tmp[y + 1][x] == "L":
				empty += 1
			if x < len(self.ins[0]) - 1:
				if self.tmp[y + 1][x + 1] == "#":
					occupied += 1
				elif self.tmp[y + 1][x + 1] == "L":
					empty += 1
		return [occupied, empty]
	def rule1(self, x, y):
		if self.tmp[y][x] == "L":
			re = self.getOccupiedAndEmpty(x, y)
			if re[0] == 0:
				self.ins[y][x] = "#"
	def rule2(self, x, y):
		if self.tmp[y][x] == "#":
			re = self.getOccupiedAndEmpty(x, y)
			if re[0] >= 4:
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
