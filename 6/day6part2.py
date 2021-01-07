class gr:
	def __init__(self):
		self.peopleCount = 0
		self.all = {}
	def add(self, line):
		self.peopleCount += 1
		for ch in line:
			if ch not in self.all:
				self.all[ch] = 1
			else:
				self.all[ch] += 1
	def cnt(self):
		c = 0
		for key in self.all:
			if self.all[key] == self.peopleCount:
				c += 1
		return c
class day6:
	def __init__(self, fileName):
		lines = open(fileName, "r").read().splitlines()
		groups = []
		group = []
		lines.append("")
		for line in lines:
			if (line == ""):
				groups.append(self.processGroup(group))
				group = []
			else:
				group.append(line)
		self.groups = groups
	def sum(self):
		sum = 0
		for gr in self.groups:
			sum += gr.cnt()
		return sum
	def processGroup(self, group):
		g = gr()
		for line in group:
			g.add(line)
		return g
task = day6("input.txt")
print (task.sum())
