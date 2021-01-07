class img:
	def __init__(self, lines):
		self.name = lines.pop(0)
		self.nr = int(self.name[5:-1])
		self.lines = [list(x) for x in lines]
		self.setBorderLines()
		self.aligned = False
	def show(self):
		for x in self.lines: print("".join(x))
	def setBorderLines(self):
		topLine = ["1" if x == "#" else "0" for x in self.lines[0]]
		rightLine = ["1" if x[len(self.lines[0]) - 1] == "#" else "0" for x in self.lines]
		botLine = ["1" if x == "#" else "0" for x in self.lines[len(self.lines)-1]]
		leftLine = ["1" if x[0] == "#" else "0" for x in self.lines]
		self.borders = [
			int("".join(topLine), 2), #top
			int("".join(rightLine), 2), #right
			int("".join(botLine), 2), #bot
			int("".join(leftLine), 2), #left
			int("".join(topLine[::-1]), 2), #topRev
			int("".join(rightLine[::-1]), 2), #rightRev
			int("".join(botLine[::-1]), 2), #botRev
			int("".join(leftLine[::-1]), 2), #leftRev
		]
	def rotClockwise(self):
		nw = [["" for y in range(len(self.lines[0]))] for x in range(len(self.lines))]
		for i in range(len(self.lines)):
			for j in range(len(self.lines[i])):
				nw[j][len(self.lines) - 1 - i] = self.lines[i][j]
		self.lines = nw
	def doVertFlip(self):
		self.lines = self.lines[::-1]
	def doHorFlip(self):
		self.lines = [ln[::-1] for ln in self.lines]
	def rotAndFlip(self, borderSum, nr): #rotate and flip img, so that borderSum checksum is on nr place (0-top, 1-right...)
		targetNr = nr - 2 if nr > 1 else nr + 2
		self.setBorderLines()
		ind = self.borders.index(borderSum)
		if ind in [4,5,6,7]:
			self.doHorFlip() if ind in [4,6] else self.doVertFlip()
			self.setBorderLines()
			ind = self.borders.index(borderSum)
		rotCnt = targetNr - ind
		if rotCnt < 0: rotCnt += 4
		while rotCnt > 0:
			self.rotClockwise()
			rotCnt -= 1
		self.setBorderLines()
		if self.borders[targetNr] != borderSum: #hackfix
			self.doHorFlip() if targetNr in [0, 2] else self.doVertFlip()
			self.setBorderLines()
	def findMonsters(self):
		monster = [[18], [0, 5, 6, 11, 12, 17, 18, 19], [1, 4, 7, 10, 13, 16]]
		cnt = 0
		for y in range(len(self.lines) - 2):
			for x in range(len(self.lines[0]) - 19):
				found = True
				for my in range(3):
					for mx in monster[my]:
						if self.lines[y + my][x + mx] != "#":
							found = False
							break
					if found == False:
						break
				if found:
					cnt += 1 #print("found a monster at: ", y, x)
		return cnt
	def getHashCount(self):
		cnt = 0
		for ln in self.lines:
			for lx in ln:
				if lx == "#":
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
		imgByNr = {}
		for imgNr in range(len(imgs)):
			imgByNr[imgs[imgNr].nr] = imgs[imgNr]
			for borderNr in range(len(imgs[imgNr].borders)):
				border = imgs[imgNr].borders[borderNr]
				if border in dic:
					dic[border].append(imgs[imgNr].nr)
				else:
					dic[border] = [imgs[imgNr].nr]
		self.imgs = imgs
		self.imgByNr = imgByNr
		self.dic = dic
		self.imgs[0].aligned = True
		self.align(self.imgs[0])
		topMost = self.goToTheEdgeByDirection(self.imgs[0], 0)
		tmp = self.goToTheEdgeByDirection(topMost, 3) #now it is topleftmost
		lns = ["Tile 9876543210:"]
		while tmp is not None:
			cur = tmp
			ln = [[],[],[],[],[],[],[],[]]
			while cur is not None:
				for lx in range(1,9):
					for ly in range(1,9):
						ln[lx-1].append(cur.lines[lx][ly])
				cur = self.getNext(cur)
			lns.extend(ln)
			tmp = self.getByDirection(tmp, 2)
		for ll in range(len(lns)):
			lns[ll] = "".join(lns[ll])
		joinedImg = img(lns)
		maxMonsters = 0
		for i1 in range(4):
			if i1 == 0:
				pass
			elif i1 == 1:
				joinedImg.doHorFlip()
			elif i1 == 2:
				joinedImg.doVertFlip()
			elif i1 == 3:
				joinedImg.doHorFlip()
				joinedImg.doVertFlip()
			for i2 in range(4):
				mcnt = joinedImg.findMonsters()
				if mcnt > maxMonsters:
					maxMonsters = mcnt
				joinedImg.rotClockwise()
		print("Monster count:", maxMonsters)
		print("Roughness of waters:", joinedImg.getHashCount() - maxMonsters * 15)
	def getNext(self, pic):
		tmp = self.getByDirection(pic, 1)
		return tmp if tmp is not None else None
	def goToTheEdgeByDirection(self, pic, dire):
		tmp = self.getByDirection(pic, dire)
		if tmp is None: return pic
		while tmp is not None:
			topMost = tmp
			tmp = self.getByDirection(topMost, dire)
		return topMost
	def getByDirection(self, pic, dire):
		if pic.borders[dire] is None:
			return None
		for candidato in self.dic[pic.borders[dire]]:
			if self.imgByNr[candidato].nr == pic.nr:
				continue
			return self.imgByNr[candidato]
	def align(self, pic):
		for borderSumIndex in range(4):
			borderSum = pic.borders[borderSumIndex]
			if borderSum is None:
				continue
			for candidato in self.dic[borderSum]:
				candidate = self.imgByNr[candidato]
				if candidate.nr == pic.nr:
					continue
				if candidate.aligned == False:
					candidate.rotAndFlip(borderSum, borderSumIndex)
					candidate.aligned = True
					self.align(candidate)
task = day20("input.txt")
