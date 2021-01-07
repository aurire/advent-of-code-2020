class day5:
	def __init__(self, fileName):
		lines = open(fileName, "r").read().splitlines()
		mx = 0
		for line in lines:
			sId = self.getSeatNum(line)
			if sId > mx:
				mx = sId
		print (mx)

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
