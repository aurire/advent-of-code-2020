class day5:
	def __init__(self, fileName):
		lines = open(fileName, "r").read().splitlines()
		self.all = []
		for line in lines:
			self.all.append(self.getSeatNum(line))
		self.all.sort()
		last = None
		for one in self.all:
			if last is None:
				last = one
			else:
				if one - 1 != last:
					print (int((last + one) / 2))
				last = one

	def getSeatNum(self, line):
		lo = 0
		hi = 127
		loCol = 0
		hiCol = 7
		for char in line:
			mid = int((hi + lo + 1) / 2)
			midCol = int((loCol + hiCol + 1) / 2)
			if char == "F":
				hi = mid - 1
			if char == "B":
				lo = mid
			if char == "L":
				hiCol = midCol - 1
			if char == "R":
				loCol = midCol
		return lo * 8 + loCol

task = day5("input.txt")
