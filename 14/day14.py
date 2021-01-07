class day14:
	def __init__(self, fName):
		self.ins = [x.split(" = ") for x in open(fName, "r").read().splitlines()]
		self.mem = {}
	def run(self):
		mask = "";
		for x in self.ins:
			if (x[0] == "mask"):
				mask = x[1]
			elif(x[0][0:4] == "mem["):
				memPlace = int(x[0][4:-1])
				val = "{0:b}".format(int(x[1]))
				newVal = []
				noOneYet = True
				for chPos in range(0, len(mask)-len(val)):
					if (noOneYet and mask[chPos]=="1"):
						noOneYet = False
					if (noOneYet == False):
						newVal.append(mask[chPos] if mask[chPos] != "X" else "0")
				for chPos in range(0, len(val)):
					if mask[-len(val)+chPos]=="X":
						newVal.append(val[chPos])
					else:
						newVal.append(mask[-len(val)+chPos])
				val = int("".join(newVal), 2)
				self.mem[memPlace] = val

task = day14("input.txt")
task.run()
sm = 0
for x in task.mem:
	sm += task.mem[x]
print(sm)
