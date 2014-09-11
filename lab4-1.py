def openFile(file):
	x = open(file, "r")
	radlista = x.readlines()
	return radlista
	x.close()

def writeFile(lista):
	x = open("crypted"+fil, "w")
	x.writelines(lista)

def rullning(fran, till):
	if fran <= till:
		return ord(till)-ord(fran)
	else:
		return ord(till)-ord(fran)+26

global fil
fil = input("Vilken fil: ")
linesFile = openFile(fil)

key = input("Skriv: ")
forskjut = rullning(key[0], key[1])
print(forskjut)


for i, s in enumerate(linesFile):
	linelist = list(s)
	for n,char in enumerate(linelist):
		linelist[n] = chr((ord(char)-ord('A')+forskjut) % 26+ord('A'))
	linesFile[i] = ''.join(linelist)
	
print(linesFile)


writeFile(linesFile)
