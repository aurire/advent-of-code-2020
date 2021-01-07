class gr:
	def __init__(self):
		self.peopleCount = 0
		self.different = set()
	def add(self, line):
		self.peopleCount += 1
		for ch in line:
			self.different.add(ch)
	def cnt(self):
		return len(self.different)
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
