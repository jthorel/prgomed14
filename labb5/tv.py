# TV class

class TV(object):

	# Standard channels into list. 
	# Each channel has it's own listitem with program as second item.
	channelList = [	["MTV", "Music Is Life"],
					["TV3", "Har du tur i kärlek?"],
	 				["SVT1", "Pengar Är Inte allt"],
	 				["TV4", "Vem Vill Inte Bli Miljonär?"]	]


	def __init__(self, namn):
		# Initializes with standard attributes, if file exist with called name, 
		# saved attributes will be loaded from file

		self.name = namn
		self.volume = 5
		self.channel = 0
		self.load()

	def load(self):
		# Loads attributes from files if file exists

		try:
			with open(self.name, "r") as fil:
				self.volume = int(fil.readline())
				self.channel = int(fil.readline())
		except:
			pass

	def save(self):
		# saves attributes to file with name of object

		with open(self.name, "w") as fil:
			fil.write(str(self.volume)+'\n')
			fil.write(str(self.channel))

	def volumeUp(self):
		# add 1 to attribute volume, only if lower than 10
		if self.volume < 10:
			self.volume += 1

	def volumeDown(self):
		# remove 1 from attribute volume, if volume is higher than 0
		if self.volume > 0:
			self.volume -= 1

	def chChannel(self, channel):
		# sets attribute channel to called argument
		self.channel = channel

