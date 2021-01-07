class day13:
	def __init__(self, fName):
		self.step = 0
		ins = open(fName, "r").read().splitlines()
		self.startTime = int(ins[0])
		ins = [x for x in ins[1].split(",")]
		self.buses = []
		for x in range(len(ins)):
			if ins[x] != "x":
				self.buses.append(int(ins[x]))
	def run(self):
		m = 9999999999
		mX = 0
		for x in self.buses:
			t = (self.startTime // x) * x
			if (t != self.startTime):
				t += x
			y = t - self.startTime
			if y < m:
				m = y
				mX = x
		print(m, mX, m*mX)

task = day13("input.txt")
task.run()
