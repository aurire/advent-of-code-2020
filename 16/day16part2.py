class day16:
	def __init__(self, fName):
		lines = open(fName, "r").read().splitlines()
		groups = [[]]
		for x in lines:
			if x == "":
				groups.append([])
			else:
				groups[len(groups) - 1].append(x)
		groups[1].pop(0)
		groups[2].pop(0)
		dic1 = {}
		for x in groups[0]:
			sp1 = x.split(": ")
			sp2 = sp1[1].split(" or ")
			for y in sp2:
				sp3 = y.split("-")
				for i in range(int(sp3[0]), int(sp3[1]) + 1):
					if i in dic1:
						dic1[i].append(sp1[0])
					else:
						dic1[i] = [sp1[0]]
		tickets = [[int(y) for y in x.split(",")] for x in groups[2]]
		mine = [int(x) for x in groups[1][0].split(",")]
		tickets.append(mine)
		invalid = []
		for y in tickets:
			for x in y:
				if x not in dic1:
					invalid.append(y)
					break
		for x in invalid:
			tickets.remove(x)
		self.tickets = tickets
		self.dic = dic1
		self.mine = mine
	def run(self):
		ln = len(self.tickets)
		candidates = []
		for x in range(len(self.tickets[0])):
			matches = {}
			for ti in self.tickets:
				if (ti[x] in self.dic):
					for zz in self.dic[ti[x]]:
						if zz in matches:
							matches[zz] += 1
						else:
							matches[zz] = 1
			candidates.append([])
			for zz in matches:
				if matches[zz] == ln:
					candidates[len(candidates) - 1].append(zz)
		removed = 1
		while removed > 0:
			removed = 0
			for x in range(len(candidates)):
				if (len(candidates[x]) == 1):
					for y in range(len(candidates)):
						if y != x and candidates[x][0] in candidates[y]:
							candidates[y].remove(candidates[x][0])
							removed += 1
		indices = []
		for x in range(len(candidates)):
			if "departure" in candidates[x][0]:
				indices.append(x)
		mult = 1
		for x in indices:
			mult *= self.mine[x]
		print (mult)
task = day16("input.txt")
task.run()

