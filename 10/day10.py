class day10:
	def __init__(self, fName):
		self.ins = open(fName, "r").read().splitlines()
		self.ins = [int(x) for x in self.ins]
		self.links = {}
		self.cache = {}
	def find(self):
		one = 0
		three = 0
		for x in range(len(self.ins)):
			if x > 0:
				if self.ins[x] - self.ins[x-1]==1:
					one += 1
				if self.ins[x] - self.ins[x-1]==3:
					three += 1
		return {
			"one": one + 1,
			"three": three + 1
		}
	def dicNlink(self):
		self.ins.append(0)
		self.ins.append(max(self.ins) + 3)
		self.ins.sort()
		for x in self.ins:
			self.links[x] = []
		for x in range(len(self.ins)):
			for y in range(len(self.ins)):
				if y > x:
					diff = self.ins[y] - self.ins[x]
					if diff in [1, 2, 3]:
						self.links[self.ins[x]].append(self.ins[y])
	def find2(self, node, target, path = ""):
		if node in self.cache:
			return self.cache[node]
		sum = 0
		for x in self.links[node]:
			if x == target:
				return 1
			else:
				sum += self.find2(x, target, path + "->"+str(x))
		self.cache[node] = sum
		return sum

task = day10("input.txt")
task.ins.sort()
print(task.ins)
rez = task.find()
print(rez["one"] * rez["three"])
print("task2----")
task.dicNlink()
print(task.find2(0, max(task.links), "0"))
