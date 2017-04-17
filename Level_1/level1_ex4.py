"""
Make a two-player Rock-Paper-Scissors game. 

Hint:
Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game


"""
import random

lista = ["papel","piedra","tijeras"]
def juego(player1,player2):

	if player1 == "papel"and player2 == "piedra" in lista:
		return 'Tu ganas'
	
	elif player1 == "piedra" and player2 == "tijeras" in lista:
		return 'Tu ganas'
	
	elif player1 == "tijeras" and player2 == "papel" in lista:
		return 'Tu ganas'
	
	elif player1 == player2 in lista:
		return 'Empate'
	
	else:
		return 'Tu pierdes'


if __name__ == '__main__':

	jugador =''
	pc =''
	new_game = 'y'
	
	while new_game != 'n':

		jugador = input('¿Quiéres jugar? Escribe piedra, papel, tijeras:  ')
		pc = random.choice(lista)
		print (pc)
		print (juego(jugador,pc))
		new_game = input("Continue: y/n ")