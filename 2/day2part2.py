class day2(object):
	def __init__(self, fileName):
		f = open(fileName, "r")
		self.lines = f.read().splitlines()
	def chk(self, psw, nums, lett):
		letcnt = 0
		num1 = int(nums[0]) - 1
		num2 = int(nums[1]) - 1
		passlen = len(psw)
		if (num1 < 0 or num2 < 0 or num1 >= passlen or num2 >= passlen):
			print ("attention, wrong number found for psw " + psw)
			return False
		let1 = psw[num1]
		let2 = psw[num2]
		if (let1 == lett):
			letcnt += 1
		if (let2 == lett):
			letcnt += 1

		return letcnt == 1
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

