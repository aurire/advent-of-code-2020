class bag:
	def __init__(self, name, canHold):
		self.name = name
		self.canHold = canHold
		self.links = {}
	def has(self, name):
		for link in self.links:
			if self.links[link].name == name or self.links[link].has(name):
				return True
		return False
	def count(self):
		if len(self.links) == 0:
			return 0
		cnt = 0
		for link in self.links:
			mult = self.canHold[self.links[link].name]
			cnt += self.links[link].count() * mult
			cnt += mult
		return cnt
class day7:
	def __init__(self, fName):
		bags = {}
		lines = open(fName, "r").read().splitlines()
		for line in lines:
			preped = self.prepLine(line)
			bags[preped[0]] = bag(preped[0], preped[1])
		self.bags = bags
		self.link()
	def prepLine(self, line):
		parts = line.split(" bags contain ")
		if parts[1] == "no other bags.":
			return [parts[0], {}]
		else:
			subParts = parts[1].split(", ")
			lastEl = len(subParts) - 1
			subParts[lastEl] = subParts[lastEl][0:-1]
			elements = {}
			for subPart in subParts:
				if (subPart[0:2] == "1 " and subPart[-4:] == " bag"):
					elements[subPart[2:-4]] = 1
				else:
					exploded = subPart.split(" ")
					num = exploded.pop(0)
					exploded.pop()
					exploded = ' '.join(exploded)
					elements[exploded] = int(num)
			return [parts[0], elements]
	def link(self):
		for bag in self.bags:
			for one in self.bags[bag].canHold:
				self.bags[bag].links[one] = self.bags[one]
	def has(self, name):
		having = []
		for bag in self.bags:
			if self.bags[bag].has(name):
				having.append(self.bags[bag].name)
		return having
task = day7("input.txt")
items = task.has("shiny gold")
print(items)
print(len(items))
shinyBag = task.bags["shiny gold"]
print (shinyBag.count())