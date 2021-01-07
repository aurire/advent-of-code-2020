class day18:
	def __init__(self):
		self.mem = []
	def simpleCalc2(self, line):
		last = ""
		ops = []
		for c in line:
			if c == " " or c == "|":
				ops.append([last, c])
				last = ""
			else:
				last += c
		ops.append([last, "="])
		for o in range(len(ops)):
			if ops[o][1] == " ":
				ops[o][1] = "D"
				ops[o + 1][0] = ops[o][0] + ops[o+1][0]
		ops = [x for x in ops if x[1] != "D"]
		while (len(ops) > 1):
			for o in range(len(ops)):
				if ops[o][1] == "|":
					ops[o][1] = "D"
					ops[o + 1][0] = [ops[o][0], ops[o+1][0]]
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
		zz = self.simpleCalc2(line)
		self.mem.append(zz)
		xz = "{" + str(len(self.mem)) + "}"
		return xz + remainder
	def lst(self, line):
		if type(line) is list :
			rez = []
			for lin in line:

				toAdd = self.lst(lin)
				if type(toAdd) is list :
					for toad in toAdd:
						rez.append(toad)
				else:
					rez.append(toAdd)
			return rez
		mode = 0
		arr = []
		st2 = ""
		for l in line:
			if mode == 0 and l != "{":
				arr.append(l)
			elif mode == 1 and l != "}":
				st2 += l
			if l == "{":
				mode = 1
			elif l == "}":
				arr.append(self.mem[int(st2) - 1])
				st2 = ""
				mode = 0
		return self.flatten(arr)
	def flatten(self, arr):
		if len(arr) == 1:
			return arr.pop()
		nw = []
		while len(arr) > 1:
			a = arr.pop(0)
			if type(a) is list:
				x = a
			else:
				x = [a]
			b = arr.pop(0)
			if type(b) is list:
				y = b
			else:
				y = [b]
			for aa in x:
				for ss in y:
					nw.append(aa+ss)
			arr.insert(0,nw)
			nw = []
		return arr.pop()
class day19:
	def __init__(self, fName):
		lines = open(fName, "r").read().splitlines()
		msgs = []
		rules = {}
		collectMsgs = False
		for line in lines:
			if line == "":
				collectMsgs = True
			else:
				if collectMsgs:
					msgs.append(line)
				else:
					spl = line.split(": ")
					rules[spl[0]] = spl[1].split(" | ")
		self.rules = rules
		self.msgs = msgs
	def expand(self, rules):
		nau = []
		for rule in rules:
			spl = rule.split(" ")
			nw = []
			for s in spl:
				if s in ['"a"', '"b"']: 
					x = s[1:-1]
				else:
					x = self.rules[s]
					if x in ['"a"', '"b"']:
						x = x[1:-1]
					else:
						if type(x) is list and len(x) == 1 and x[0] in ['"a"', '"b"']:
							x = x[0][1:-1]
						else:
							x = "(" + self.expand(x) + ")"
				nw.append(x)
			nau.append(" ".join(nw))
		return " | ".join(nau)
for xxx in ["42", "31"]:
	task = day19("input.txt")
	formula = task.expand(task.rules[xxx])
	t2 = day18()
	rr = t2.calc(formula)
	zzz = t2.lst(rr)
	hazz = False
	for zzzz in zzz:
		if "{" in zzzz:
			hazz = True
			break
	while hazz:
		zzz = t2.lst(zzz)
		hazz = False
		for zzzz in zzz:
			if "{" in zzzz:
				hazz = True
				break
	sm = 0
	for ms in task.msgs:
		if ms in zzz:
			sm += 1
	print("part2:", xxx)
	print(zzz)
	print("-----")
