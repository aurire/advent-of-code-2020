class day15:
	def __init__(self, fName):
		self.ins = [int(x) for x in open(fName, "r").read().split(",")]
		self.mem = {}
		for x in range(len(self.ins)-1):
			self.mem[self.ins[x]] = x
	def run(self, target):
		x = len(self.ins) - 1
		while x < target - 1:
			cur = self.ins[x]
			if cur in self.mem:
				dif = x-self.mem[cur]
				self.ins.append(dif)
				self.mem[cur] = x
			else:
				self.ins.append(0)
				self.mem[cur] = x
			x += 1
task = day15("input.txt")
task.run(2020)
print("part1", task.ins[len(task.ins) - 1])
task.run(30000000)
print("part2", task.ins[len(task.ins) - 1])
