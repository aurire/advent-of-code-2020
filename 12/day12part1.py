class day12:
	def __init__(self, fName):
		self.step = 0
		self.ins = [[x[:1], int(x[1:])] for x in open(fName, "r").read().splitlines()]
		self.x = 0
		self.y = 0
		self.curDir = "E"
		self.dirs = ["N", "E", "S", "W"]
		self.dirMap = {"N": 0, "E": 1, "S": 2, "W": 3}
	def mv(self, ins, num):
		if "N" == ins:
			self.y -= num
		elif "S" == ins:
			self.y += num
		elif "E" == ins:
			self.x += num
		elif "W" == ins:
			self.x -= num
	def rt(self, ins):
		c = self.dirMap[self.curDir]
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
		self.curDir = self.dirs[c]
	def rot(self, ins, num):
		for i in range(int(num / 90)):
			self.rt(ins)
	def doCmd(self, ins, num):
		if ins in ["N", "S", "E", "W"]:
			self.mv(ins, num)
		elif ins in ["L", "R"]:
			self.rot(ins, num)
		elif "F" == ins:
			self.mv(self.curDir, num)
	def run(self):
		for cmd in self.ins:
			self.doCmd(cmd[0], cmd[1])
task = day12("input.txt")
task.run()
print("x", task.x, "y", task.y, "manh", task.x + task.y)