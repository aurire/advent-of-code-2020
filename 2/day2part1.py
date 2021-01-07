class day2(object):
	def __init__(self, fileName):
		f = open(fileName, "r")
		self.lines = f.read().splitlines()
	def chk(self, psw, nums, lett):
		letcnt = 0
		for one in psw:
			if (one == lett):
				letcnt += 1
		if (letcnt < int(nums[0]) or letcnt > int(nums[1])):
			return False
		return True
	def validate(self):
		cnt = 0
		for line in self.lines:
			spl = line.split(" ")
			nums = spl[0].split("-")
			lett = spl[1].split(":")[0]
			psw = spl[2]
			if (self.chk(psw, nums, lett)):
				cnt += 1
		print (cnt)
puzzle = day2("input.txt")
puzzle.validate()
#print(puzzle.lines)

