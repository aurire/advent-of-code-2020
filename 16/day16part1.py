class day16:
	def __init__(self, fName):
		lines = open(fName, "r").read().splitlines()
		groups = [[]]
		for x in lines:
			if x == "":
				groups.append([])
			else:
				groups[len(groups) - 1].append(x)
		groups[1].pop(0)
		groups[2].pop(0)
		dic1 = {}
		for x in groups[0]:
			sp1 = x.split(": ")
			sp2 = sp1[1].split(" or ")
			for y in sp2:
				sp3 = y.split("-")
				for i in range(int(sp3[0]), int(sp3[1]) + 1):
					if i in dic1:
						dic1[i].append(sp1[0])
					else:
						dic1[i] = [sp1[0]]
		tickets = [[int(y) for y in x.split(",")] for x in groups[2]]
		invalid = []
		for y in tickets:
			for x in y:
				if x not in dic1:
					invalid.append(x)
		print(invalid)
		print(sum(invalid))
task = day16("input.txt")
