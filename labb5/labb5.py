
from tv import TV

def loadTVs():
	# Creates string-list from file 'tvapparater'
	# PRE: none
	# POST: list of strings

	with open("tvapparater", "r") as fil:
		tvList = fil.readlines()
	for i in range(len(tvList)):
		tvList[i] = tvList[i].rstrip("\n")
	return tvList


def createTVObjects(tvList):
	# Creates a list of TV objects
	# PRE: list of strings
	# POST: list of objects of TV

	for i, s in enumerate(tvList):
		tvObjects.append(TV(s))


def chooseTV(tvObjects): 
	# MAIN-MENU
	# PRE: List of TV objects
	# POST: prints

	loop = 1	
	while loop == 1:
		print("-----------")
		print("Vilken TV?")
		for i, f in enumerate(tvList):
			print(str(i+1)+". "+f)
		print("\nq: Avsluta och spara")
		print("-----------")

		try:
			val = input("Vilken TV (nr): ")
			val = int(val) - 1
			tvMenu(tvObjects[val])				
		except IndexError:
			print("Finns inte, försök igen")
		except ValueError:
			if val == 'q':
				for i in range(len(tvObjects)):
					tvObjects[i].save()
				quit()
				break
			else:
				print("Skriv en siffra!")


def changeChannel(tvObject):	
	# Change channel in 1 object of class TV
	# PRE: 1 object of class TV
	# POST: modify the attribute 'channel' in class TV

	print("-----------")
	for i in range(len(tvObject.channelList)):
		print(str(i+1)+". "+tvObject.channelList[i][0])
	print("-----------")

	cloop = 1
	while cloop == 1:
		valc = input("Vilken kanal?: ")
		try:
			valc = int(valc)			
			tvObject.channelList[valc-1]
			tvObject.chChannel(valc-1)
			cloop = 0
		except:
			print("Välj en kanal genom siffran")
			

def tvMenu(tvObject):	
	# Show information about and modify a specific TV object
	# PRE: 1 object of class TV
	# POST: prints

	tvloop = 1
	while tvloop == 1:
		print("-----------")
		printTV(tvObject)
		print("1. Byt kanal")
		print("2. Höj volymen")
		print("3. Sänk volymen")
		print("4. Tillbaka till huvudmenyn")
		print("-----------")
		vald = input("Ange val: ")
		try:
			vald = int(vald)
			if vald == 1:
				changeChannel(tvObject)
			elif vald == 2:
				tvObject.volumeUp()
			elif vald == 3:
				tvObject.volumeDown()
			elif vald == 4:
				tvloop = 0
			else:
				print("\nFEL VAL, FÖRSÖK IGEN")
		except ValueError:
			print("\nVÄLJ EN SIFFRA")


def printTV(tvObject):	
	# Prints information about an object of the class TV
	# PRE: 1 object of class TV
	# POST: prints

	print(tvObject.name+":")
	print("Kanal: " + tvObject.channelList[tvObject.channel][0])
	print("Program: " + tvObject.channelList[tvObject.channel][1])
	print("Volym: " + str(tvObject.volume), '\n')


# Initialization
tvObjects = []	
tvList = loadTVs()
createTVObjects(tvList)

# Run main-menu
chooseTV(tvObjects)

# Safe-save
for i in range(len(tvObjects)):
	tvObjects[i].save()

