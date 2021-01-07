class img:
	def __init__(self, lines):
		self.name = lines.pop(0)
		self.nr = int(self.name[5:-1])
		self.lines = [list(x) for x in lines]
		self.setBorderLines()
	def show(self):
		for x in self.lines:
			print("".join(x))
	def setBorderLines(self):
		topLine = ["1" if x == "#" else "0" for x in self.lines[0]]
		rightLine = ["1" if x[len(self.lines[0]) - 1] == "#" else "0" for x in self.lines]
		botLine = ["1" if x == "#" else "0" for x in self.lines[len(self.lines)-1]]
		leftLine = ["1" if x[0] == "#" else "0" for x in self.lines]
		topLineRev = topLine[::-1]
		rightLineRev = rightLine[::-1]
		botLineRev = botLine[::-1]
		leftLineRev = leftLine[::-1]
		self.borders = [
			int("".join(topLine), 2), #top
			int("".join(rightLine), 2), #right
			int("".join(botLine), 2), #bot
			int("".join(leftLine), 2), #left
			int("".join(topLineRev), 2), #topRev
			int("".join(rightLineRev), 2), #rightRev
			int("".join(botLineRev), 2), #botRev
			int("".join(leftLineRev), 2), #leftRev
		]
		self.connections = [
			None,
			None,
			None,
			None
		]
	def calcBorders(self):
		cnt = 0
		for c in self.connections:
			if c is not None:
				cnt += 1
		return cnt
class day20:
	def __init__(self, fName):
		imgs = []
		lines = open(fName, "r").read().splitlines()
		lns = []
		dic = {}
		for line in lines:
			if line == "":
				imgs.append(img(lns))
				lns = []
			else:
				lns.append(line)
		imgs.append(img(lns))
		for imgNr in range(len(imgs)):
			im = imgs[imgNr]
			for borderNr in range(len(im.borders)):
				border=im.borders[borderNr]
				if border in dic:
					dic[border].append([imgNr, borderNr])
				else:
					dic[border] = [[imgNr, borderNr]]
		for dicNr in dic:
			if len(dic[dicNr]) == 2:
				if dic[dicNr][0][1] in [0,4]:
					imgs[dic[dicNr][0][0]].connections[0] = dic[dicNr][1]
				elif dic[dicNr][0][1] in [1,5]:
					imgs[dic[dicNr][0][0]].connections[1] = dic[dicNr][1]
				elif dic[dicNr][0][1] in [2,6]:
					imgs[dic[dicNr][0][0]].connections[2] = dic[dicNr][1]
				elif dic[dicNr][0][1] in [3,7]:
					imgs[dic[dicNr][0][0]].connections[3] = dic[dicNr][1]
				if dic[dicNr][1][1] in [0,4]:
					imgs[dic[dicNr][1][0]].connections[0] = dic[dicNr][0]
				elif dic[dicNr][1][1] in [1,5]:
					imgs[dic[dicNr][1][0]].connections[1] = dic[dicNr][0]
				elif dic[dicNr][1][1] in [2,6]:
					imgs[dic[dicNr][1][0]].connections[2] = dic[dicNr][0]
				elif dic[dicNr][1][1] in [3,7]:
					imgs[dic[dicNr][1][0]].connections[3] = dic[dicNr][0]
		mult = 1
		for im in imgs:
			if im.calcBorders() == 2:
				mult *= im.nr
		print(mult)
task = day20("input.txt")
