class day3(object):
	def __init__(self, fileName):
		self.lines = open(fileName, "r").read().splitlines()
		pass
	def slide(self, py, px):
		end = len(self.lines)
		endX = len(self.lines[0])
		cur = 0
		curX = 0
		hits = 0
		while (cur < end):
			square = self.lines[cur][curX]
			if (square == "#"):
				hits += 1
			curX += px
			if (curX >= endX):
				curX -= endX
			cur += py
		return hits
task = day3("input.txt")
print (task.slide(1, 1) * task.slide(1, 3) * task.slide(1, 5) * task.slide(1, 7) * task.slide(2, 1))
