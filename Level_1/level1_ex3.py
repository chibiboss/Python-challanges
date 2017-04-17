"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.

Hint
Use __init__ method to construct some parameters


"""

class Palabra:
	def __init__(self, letras):
		self.letras = letras

	def getString(self):			
		texto = input("introduce texto: ")
		self.letras = texto
		return texto
	
	def printString(self):
		return self.letras.upper()

if __name__== '__main__':
	a = Palabra("")
	a.getString()
	print (a.printString())