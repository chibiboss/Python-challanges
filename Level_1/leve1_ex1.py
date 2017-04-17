"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method

"""

if __name__ == '__main__':
	begin = int(input("Ingrese rango de inicio "))
	end = int(input("Ingrese rango final "))
	lista = []
	for x in range(begin, end):
			if x % 7 == 0 and x % 5 != 0:
				lista.append(x)
	print(lista)  	