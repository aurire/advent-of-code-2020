class day21:
	def __init__(self, fName):
		lines = open(fName).read().splitlines()
		dic = {}
		dicIng = {}
		for lineN in range(len(lines)):
			lines[lineN] = lines[lineN].split(" (contains ")
			lines[lineN][0] = lines[lineN][0].split(" ")
			for ing in lines[lineN][0]:
				if ing in dicIng:
					dicIng[ing] += 1
				else:
					dicIng[ing] = 1
			lines[lineN][1] = lines[lineN][1][0:-1].split(", ")
			for alergen in lines[lineN][1]:
				if alergen in dic:
					dic[alergen].extend(lines[lineN][0].copy())
				else:
					dic[alergen] = lines[lineN][0].copy()
		self.dic= dic
		self.lines = lines
		for i in range(100):
			for line in lines:
				for ale in line[1]:
					for aleOne in dic[ale]:
						if aleOne not in line[0]:
							dic[ale].remove(aleOne)
		sm = 0
		for ing in dicIng:
			inc = False
			for ale in dic:
				if ing in dic[ale]:
					inc = True
					break
			if inc == False:
				sm += dicIng[ing]
		print(sm)
task = day21("input.txt")
# print(task.lines)
