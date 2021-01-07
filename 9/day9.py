class day9:
	def __init__(self, fName):
		self.ins = open(fName, "r").read().splitlines()
	def canSumTo(self, preamble, target):
		for x in range(len(preamble)):
			for y in range(len(preamble)):
				if x != y:
					if int(preamble[x]) + int(preamble[y]) == int(target):
						return True
		return False
	def find(self, preambleSize):
		preamble = []
		for one in self.ins:
			if len(preamble) == preambleSize:
				if (self.canSumTo(preamble, one) == False):
					print (one)
					return int(one)
				preamble.pop(0)
			preamble.append(one)
	def find2(self, target):
		for howManyToSum in range(2, len(self.ins)):
			for pos in range(howManyToSum - 1, len(self.ins)):
				sumlist = [int(self.ins[pos-z]) for z in range(howManyToSum)]
				if sum(sumlist) == target:
					print(sumlist, target)
					return sumlist
task = day9("input.txt")
lst = task.find2(task.find(25))
print(min(lst) + max(lst))
