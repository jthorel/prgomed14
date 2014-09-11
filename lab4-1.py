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
<<<<<<< HEAD
		linelist[n] = chr((ord(char)-ord('A')+forskjut) % 26+ord('A'))
=======
		if char.isupper():
			linelist[n] = chr((ord(char)-ord('A')+forskjut) % 26+ord('A'))
>>>>>>> b62406f9b60053df23bee862756ad070a29a2302
	linesFile[i] = ''.join(linelist)
	
print(linesFile)


<<<<<<< HEAD
=======
	
		


>>>>>>> b62406f9b60053df23bee862756ad070a29a2302
writeFile(linesFile)
