class day18:
	def __init__(self, fName):
		self.lines = [int(x) for x in [self.calc(x) for x in open(fName, "r").read().splitlines()]]
	def simpleCalc2(self, line):
		last = ""
		ops = []
		for c in line:
			if c == "+" or c == "*":
				ops.append([int(last), c])
				last = ""
			elif c.isdigit():
				last += c
		ops.append([int(last), "="])
		for o in range(len(ops)):
			if ops[o][1] == "+":
				ops[o][1] = "D"
				ops[o + 1][0] = ops[o][0] + ops[o+1][0]
		ops = [x for x in ops if x[1] != "D"]
		while (len(ops) > 1):
			for o in range(len(ops)):
				if ops[o][1] == "*":
					ops[o][1] = "D"
					ops[o + 1][0] = ops[o][0] * ops[o+1][0]
			ops = [x for x in ops if x[1] != "D"]
		return ops[0][0]
	def calc(self, line):
		openParPos = line.find('(')
		if openParPos != -1:
			line = line[0:openParPos] + self.calc(line[openParPos+1:])
		remainder = ""
		endParPos = line.find(')')
		if endParPos != -1:
			remainder = line[endParPos+1:]
			line = line[0:endParPos]
		return str(self.simpleCalc2(line)) + remainder
task = day18("input.txt")
print(sum(task.lines))