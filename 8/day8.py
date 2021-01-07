class app:
	def __init__(self, fName):
		self.acc = 0
		self.pos = 0
		self.ins = [x.split(" ") for x in open(fName, "r").read().splitlines()]
		for x in self.ins:
			x.append(0)
	def getCur(self):
		return self.ins[self.pos][1]
	def beforeCall(self):
		self.ins[self.pos][2] += 1
		if self.ins[self.pos][2] > 1:
			self.state = 0
	def fn_jmp(self):
		self.pos += int(self.getCur()) - 1
	def fn_nop(self):
		pass
	def fn_acc(self):
		self.acc += int(self.getCur())
	def run(self):
		self.state = 1
		cnt = len(self.ins)
		while self.state == 1 and self.pos < cnt:
			fn = getattr(self, "fn_" + self.ins[self.pos][0])
			self.beforeCall()
			if self.state:
				fn()
			self.pos += 1
task = day8("test.txt")
task.run()
for k in range(len(task.ins)):
	if task.ins[k][0] in ["jmp", "nop"]:
		task.ins[k][0] = "nop" if task.ins[k][0] == "jmp" else "jmp"
		task.run()
		if task.state == 1:
			print("found", self.acc
		task.ins[k][0] = "nop" if task.ins[k][0] == "jmp" else "jmp"
print(task.acc)