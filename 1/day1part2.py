class day1(object):
	def __init__(self, fName):
		f = open(fName, "r")
		lines = f.read().splitlines()
		self.lines = []
		for line in lines:
			self.lines.append(int(line))
	def find(self, target):
		for line in self.lines:
			other = self.lines.copy()
			other.remove(line)
			for line2 in other:
				lines3 = other.copy()
				lines3.remove(line2)
				for line3 in lines3:
					if (line + line2 + line3 == target):
						return [line, line2, line3]
task1 = day1("input.txt")
items = task1.find(2020)
print(items[0] * items[1] * items[2])
