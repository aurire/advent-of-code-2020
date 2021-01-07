class day17:
	def __init__(self, fName):
		lines = [list(x) for x in open(fName, "r").read().splitlines()]
		y = 0
		space = {}
		for line in lines:
			x = 0
			space[y] = {}
			for dot in line:
				space[y][x] = dot
				x += 1
			y += 1
		self.space = {}
		self.space[0] = space
	def getPix(self, z, y, x):
		if z in self.space and y in self.space[z] and x in self.space[z][y]:
			return self.space[z][y][x]
		return "."
	def setPix2(self, z, y, x, dot):
		self.toSet.append([z,y,x,dot])
	def setPix(self, z, y, x, dot):
		if z in self.space and y in self.space[z] and x in self.space[z][y]:
			self.space[z][y][x] = dot
		else:
			if z not in self.space:
				self.space[z] = {}
			if y not in self.space[z]:
				self.space[z][y] = {}
			if x not in self.space[z][y]:
				self.space[z][y][x] = {}
			self.space[z][y][x] = dot
	def neighbCoords(self, z, y, x):
		return [
			[z-1, y-1, x-1], [z-1, y-1, x], [z-1, y-1, x+1],  [z-1, y, x-1], [z-1, y, x], [z-1, y, x+1],  [z-1, y+1, x-1], [z-1, y+1, x], [z-1, y+1, x+1],
			[z+1, y-1, x-1], [z+1, y-1, x], [z+1, y-1, x+1],  [z+1, y, x-1], [z+1, y, x], [z+1, y, x+1],  [z+1, y+1, x-1], [z+1, y+1, x], [z+1, y+1, x+1],
			[z, y-1, x-1], [z, y-1, x], [z, y-1, x+1],  [z, y, x-1], [z, y, x+1], [z, y+1, x-1],  [z, y+1, x], [z, y+1, x+1],
		]
	def activeCnt(self, arr):
		cnt = 0
		for coords in arr:
			if self.getPix(coords[0], coords[1], coords[2]) == "#":
				cnt += 1
		return cnt
	def checkFix(self, oz, oy, ox):
		neigh = self.neighbCoords(oz, oy, ox)
		aCnt = self.activeCnt(neigh)
		if self.getPix(oz, oy, ox) == "#" and aCnt != 2 and aCnt != 3:
			self.setPix2(oz, oy, ox, ".")
		elif self.getPix(oz, oy, ox) == "." and aCnt == 3:
			self.setPix2(oz, oy, ox, "#")
		return neigh
	def cnt(self):
		cnt = 0
		for oz in self.space:
			for oy in self.space[oz]:
				for ox in self.space[oz][oy]:
					if self.space[oz][oy][ox] == "#":
						cnt += 1
		return cnt
	def run(self):
		self.toSet = []
		toCheck = {}
		for oz in self.space:
			for oy in self.space[oz]:
				for ox in self.space[oz][oy]:
					neigh = self.checkFix(oz, oy, ox)
					toCheck[str(oz)+"|"+str(oy)+"|"+str(ox)] = 1
					for n in neigh:
						if str(n[0])+"|"+str(n[1])+"|"+str(n[2]) not in toCheck:
							toCheck[str(n[0])+"|"+str(n[1])+"|"+str(n[2])] = 0
		for c in toCheck:
			if toCheck[c] == 1:
				continue
			spl = c.split("|")
			self.checkFix(int(spl[0]), int(spl[1]), int(spl[2]))
		for xx in self.toSet:
			self.setPix(xx[0],xx[1],xx[2],xx[3])
task = day17("input.txt")
print(task.cnt())
task.run()
task.run()
task.run()
task.run()
task.run()
task.run()
print(task.cnt())
