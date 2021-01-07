class day18:
	def __init__(self, fName):
		self.lines = [int(x) for x in [self.calc(x) for x in open(fName, "r").read().splitlines()]]
	def simpleCalc(self, line):
		last = ""
		rez = None
		for c in line:
			if c == "+" or c == "*":
				last = int(last)
				rez = int(last) if rez is None else (rez * last if op == "*" else rez + last)
				op = c
				last = ""
			elif c.isdigit():
				last += c
		rez = rez * int(last) if op == "*" else rez + int(last)
		return rez
	def calc(self, line):
		openParPos = line.find('(')
		if openParPos != -1:
			line = line[0:openParPos] + self.calc(line[openParPos+1:])
		remainder = ""
		endParPos = line.find(')')
		if endParPos != -1:
			remainder = line[endParPos+1:]
			line = line[0:endParPos]
		return str(self.simpleCalc(line)) + remainder
task = day18("input.txt")
print(sum(task.lines))