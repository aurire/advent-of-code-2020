class day12:
	def __init__(self, fName):
		self.step = 0
		self.ins = [[x[:1], int(x[1:])] for x in open(fName, "r").read().splitlines()]
		self.x = 0
		self.y = 0
		self.curDir = ["E", 10, "N", 1]
		self.dirs = ["N", "E", "S", "W"]
		self.dirMap = {"N": 0, "E": 1, "S": 2, "W": 3}
	def mv2(self, ins, num):
		if "N" == ins:
			if self.curDir[2] == "N":
				self.curDir[3] += num
			else:
				self.curDir[3] -= num
				if self.curDir[3] < 0:
					self.curDir[2] = "N"
					self.curDir[3] = -self.curDir[3]
		elif "S" == ins:
			if self.curDir[2] == "S":
				self.curDir[3] += num
			else:
				self.curDir[3] -= num
				if self.curDir[3] < 0:
					self.curDir[2] = "S"
					self.curDir[3] = -self.curDir[3]
		if "W" == ins:
			if self.curDir[0] == "W":
				self.curDir[1] += num
			else:
				self.curDir[1] -= num
				if self.curDir[1] < 0:
					self.curDir[0] = "W"
					self.curDir[1] = -self.curDir[1]
		elif "E" == ins:
			if self.curDir[0] == "E":
				self.curDir[1] += num
			else:
				self.curDir[1] -= num
				if self.curDir[1] < 0:
					self.curDir[0] = "E"
					self.curDir[1] = -self.curDir[1]
	def mv(self, num):
		if (self.curDir[0] == "E"):
			self.x += self.curDir[1] * num
		else:
			self.x -= self.curDir[1] * num
		if (self.curDir[2] == "S"):
			self.y += self.curDir[3] * num
		else:
			self.y -= self.curDir[3] * num
	def rt2(self, curDir, ins):
		c = self.dirMap[curDir]
		if "R" == ins:
			if c == 3:
				c = 0
			else:
				c += 1
		elif "L" == ins:
			if c == 0:
				c = 3
			else:
				c -= 1
		return self.dirs[c]
	def rt(self, ins):
		self.curDir[0] = self.rt2(self.curDir[0], ins)
		self.curDir[2] = self.rt2(self.curDir[2], ins)
		if self.curDir[0] in ["N", "S"]:
			t1 = self.curDir[0]
			t2 = self.curDir[1]
			self.curDir[0] = self.curDir[2]
			self.curDir[1] = self.curDir[3]
			self.curDir[2] = t1
			self.curDir[3] = t2
	def rot(self, ins, num):
		for i in range(int(num / 90)):
			self.rt(ins)
	def doCmd(self, ins, num):
		if ins in ["N", "S", "E", "W"]:
			self.mv2(ins, num)
		elif ins in ["L", "R"]:
			self.rot(ins, num)
		elif "F" == ins:
			self.mv(num)
		print(ins, num, self.x, self.y, self.curDir)
	def run(self):
		for cmd in self.ins:
			self.doCmd(cmd[0], cmd[1])
task = day12("input.txt")
print(task.x, task.y, task.curDir)
print(task.curDir)
task.run()
print("x", task.x, "y", task.y, "manh", abs(task.x) + abs(task.y))