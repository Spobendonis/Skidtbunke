from Game import Game
from Player import HumanController, AIController

def Main():
	p1 = HumanController()
	p2 = AIController()
	
	players = [p1, p2]

	game = Game(row_count=6, deck_count=6, max_card=16, players=players)
	# game.print_info()
	game.play()

if __name__ == "__main__":
	Main()