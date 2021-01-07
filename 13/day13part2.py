import math
class day13:
	def findCrossing(self, num1, num2, numInQueue):
		x = num1
		y = num2
		while y != x + numInQueue:
			if y > x + numInQueue:
				x += num1
			else:
				y += num2
		return x
	def findCrossingsAndMultipliers(self, input):
		buses = [-1 if x == "x" else int(x) for x in input]
		crosspointsAndMultipliers = []
		for busIndex in range(1, len(buses)):
			if buses[busIndex] != -1:
				crosspointsAndMultipliers.append([
					task.findCrossing(buses[0], buses[busIndex], busIndex),
					buses[0] * buses[busIndex] // math.gcd(buses[0], buses[busIndex])
				])
		return crosspointsAndMultipliers;
	def merge(self, num1, num2, multiplier1, multiplier2):
		while num1 != num2:
			if num1 > num2:
				num2 += multiplier2
			else:
				num1 += multiplier1
		return num1
	def getCorrectCrossing(self, fName):
		busesInput = open(fName, "r").read().splitlines().pop().split(",")
		crosses = self.findCrossingsAndMultipliers(busesInput)
		while(len(crosses) > 1):
			crosses.append([
				self.merge(crosses[0][0], crosses[1][0], crosses[0][1], crosses[1][1]),
				crosses[0][1] * crosses[1][1] // math.gcd(crosses[0][1], crosses[1][1])
			])
			del crosses[:2]
		return crosses[0][0]
task = day13()
print(task.getCorrectCrossing("input.txt"))