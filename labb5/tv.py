# TV class

class TV(object):

	channelList = [	["MTV", "Music Is Life"],
					["TV3", "Har du tur i kärlek?"],
	 				["SVT1", "Pengar Är Inte allt"],
	 				["TV4", "Vem Vill Inte Bli Miljonär?"]	]


	def __init__(self, namn):
		self.name = namn
		self.volume = 5
		self.channel = 0
		self.load()

	def load(self):
		try:
			with open(self.name, "r") as fil:
				self.volume = int(fil.readline())
				self.channel = int(fil.readline())
		except:
			pass

	def save(self):
		with open(self.name, "w") as fil:
			fil.write(str(self.volume)+'\n')
			fil.write(str(self.channel))

	def volumeUp(self):
		if self.volume < 10:
			self.volume += 1

	def volumeDown(self):
		if self.volume > 0:
			self.volume -= 1

	def chChannel(self, channel):
		self.channel = channel

