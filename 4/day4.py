class passport(object):
	def __init__(self, pars):
		self.ecl = None
		self.pid = None
		self.eyr = None
		self.hcl = None
		self.byr = None
		self.iyr = None
		self.cid = None
		self.hgt = None
		for param in pars:
			par = param.split(":")
			if (par[0] == "ecl"):
				self.ecl = par[1]
			elif (par[0] == "pid"):
				self.pid = par[1]
			elif (par[0] == "eyr"):
				self.eyr = par[1]
			elif (par[0] == "hcl"):
				self.hcl = par[1]
			elif (par[0] == "byr"):
				self.byr = par[1]
			elif (par[0] == "iyr"):
				self.iyr = par[1]
			elif (par[0] == "cid"):
				self.cid = par[1]
			elif (par[0] == "hgt"):
				self.hgt = par[1]
	def hasAllDigits(self, x):
		for c in x:
			if (c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
				return False
		return True
	def isAllHex(self, x):
		for c in x:
			if (c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]):
				return False
		return True
	def isValid(self):
		if (
			self.hgt is None or self.iyr is None or self.byr is None or self.hcl is None
			or self.eyr is None or self.pid is None or self.ecl is None
		):
			return False
		if (self.hasAllDigits(self.byr) == False or len(self.byr) != 4 or int(self.byr) < 1920 or int(self.byr) > 2002):
			return False
		if (self.hasAllDigits(self.iyr) == False or len(self.iyr) != 4 or int(self.iyr) < 2010 or int(self.iyr) > 2020):
			return False
		if (self.hasAllDigits(self.eyr) == False or len(self.eyr) != 4 or int(self.eyr) < 2020 or int(self.eyr) > 2030):
			return False
		if (self.hgt[-2:] != "cm" and self.hgt[-2:] != "in"):
			return False
		if (self.hgt[-2:] == "cm" and (int(self.hgt[0:-2]) < 150 or int(self.hgt[0:-2]) > 193)):
			return False
		if (self.hgt[-2:] == "in" and (int(self.hgt[0:-2]) < 59 or int(self.hgt[0:-2]) > 76)):
			return False
		if (len(self.hcl) != 7 or self.hcl[0:1] != "#" or self.isAllHex(self.hcl[1:]) == False):
			return False
		if (self.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
			return False
		if (self.hasAllDigits(self.pid) == False or len(self.pid) != 9):
			return False
		return True

class day4(object):
	def __init__(self, fileName):
		lines = open(fileName, "r").read().splitlines()
		lcnt = len(lines)
		l = 0
		oneData = ""
		passports = []
		while l <= lcnt:
			if (lcnt == l):
				line = ""
			else:
				line = lines[l]
			if (line == ""):
				passports.append(passport(oneData.split(" ")))
				oneData = ""
			if (oneData == ""):
				oneData = line
			else:
				oneData = oneData + " " + line
			l += 1
		self.passports = passports
	def countValid(self):
		cnt = 0
		for p in task.passports:
			if p.isValid():
				cnt += 1
		return cnt

task = day4("input.txt")
print(task.countValid())
