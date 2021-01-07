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
		for i in range(10):
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
		for d in dic:
			dic[d] = list(set(dic[d]))
		noop = False
		while noop == False:
			noop = True
			for d in dic:
				if len(dic[d]) == 1:
					for d2 in dic:
						if d2 != d:
							if dic[d][0] in dic[d2]:
								dic[d2].remove(dic[d][0])
								noop = False
		lst = []
		for d in dic:
			lst.append(d)
		lst = sorted(lst)
		lst2 = []
		for l in lst:
			lst2.append(dic[l].pop())
		print(",".join(lst2))
task = day21("input.txt")