import random
from Player import Controller

class Game():
	def __init__(self, row_count: int, deck_count: int, max_card: int, players: list[Controller]):
		self.row_count = row_count
		self.deck_count = deck_count
		self.max_card = max_card
		self.players = players

		self.reserve = [i+1 for _ in range(deck_count) for i in range(max_card)]
		random.shuffle(self.reserve)

		for player in players:
			player.init(row_count, deck_count, max_card)
	
	def play(self):
		while(len(self.reserve) > 0):
			card = self.reserve.pop()
			for p in self.players:
				p.play(card)
		for i, p in enumerate(self.players):
			if p.won_game():
				print(f"Player {i} has won!")
			else:
				print(f"Player {i} has lost!")

	def print_info(self):
		print(f"Row Count: {self.row_count}, Deck Count: {self.deck_count}, Max Card: {self.max_card}, Player Count: {len(self.players)}")