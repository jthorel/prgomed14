# UPPGIFT 1
global CONST_g
CONST_g = 9.8

def falling_distance(tid):
    return ((CONST_g*tid**2)/2)

i = 1
print('Tid(s) - Fallsträcka(m)')
while i <= 10:
    print(i, falling_distance(i))
    i = i+1



#UPPGIFT 2


# - FUNCTIONS -
# Läser fil och matar en global lista med alla rader från fil


def readFile(file):
	"""
	>>> isStrInt("11")
	True
	>>> isStrInt("1a")
	False
	>>> isStrInt("fofk ad")
	False
	>>> isStrInt("123 4 11")
	False
	"""
	global radlista
	radlista = file.readlines()

# Testar att öppna givet filnamn
def openFile(file):
	"""
	>>> openFile("tal.txt")
	True
	>>> openFile("awdaw")
	False
	>>> openFile("111.txt")
	False
	>>> openFile("123 4 11")
	False
	"""
	try: 
		x = open(file, "r")
		readFile(x)
		x.close()
		return True
	except IOError:
		return False

def median(list):
	"""
	>>> median([1,5,13])
	5
	>>> median([1,6,2,9,2])
	2
	"""
	return sorted(list)[len(list)//2]

# Medelvärde av en lista av tal
def medelVarde(list):
	"""
	>>> medelVarde([1,6,2,9,2])
	4.0
	>>> medelVarde([1,5,13])
	6.333333333333333
	"""
	i,n=0, 0
	for i in list:
		n = n + i
	return n/len(list)


# Kollar om en lista endast är tal
def isStrInt(lista):
	"""
	DOCTEST
	>>> isStrInt("11")
	True
	>>> isStrInt("1a")
	False
	>>> isStrInt("fofk ad")
	False
	>>> isStrInt("123 4 11")
	False
	"""
	ord = ''.join(lista)
	try:
		ord = int(ord)
		return True
	except:
		return False



# - MAIN -
# Input av fil av användare, loopar tills det är lyckat
file = input("Filnamn: ")
x=1
while x==1:
	if openFile(file):
		x=0
	else:
		file = input("Det funkade inte, försök igen: ")

# Hämtar tal från rader och skriver ut rader som är strängar
numLista = []
index=1
for line in radlista:
	line.rstrip('\n')
	try:
		numLista.append(int(line))					
	except:
		lineSplit = line.split()
		if isStrInt(lineSplit):
			for ord in lineSplit:
				numLista.append(int(ord))
		else:
			for ord in lineSplit:
				try:
					numLista.append(int(ord))
				except:
					pass
			print("Rad", index, line)

	index = index+1

# Skriv ut svaren
numListasorted = sorted(numLista)
print("Medelvärdet är",medelVarde(numListasorted))
print("Medianen är",median(numListasorted))
print("Största värdet är",numListasorted[-1])
print("Minsta värdet är",numListasorted[0])

def _test():
    import doctest
    doctest.testmod()
 
if __name__ == "__main__":
    _test()
