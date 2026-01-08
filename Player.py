import numpy as np

class Controller():
	def __init__(self):
		pass

	def init(self, row_count, deck_count, max_card):
		self.row_count = row_count
		self.deck_count = deck_count
		self.max_card = max_card

		self.rows = [[] for _ in range(row_count)]
		self.decks = [0 for _ in range(deck_count)]

	def play(self, card):
		pass

	def won_game(self):
		for d in self.decks:
			if d != self.max_card:
				return False
		return True

	def place_card_on_row(self, card:int, row:int):
		self.rows[row-1].append(card)
	
	def place_card_on_deck(self, card:int, deck:int):
		if self.decks[deck-1] + 1 == card:
			self.decks[deck-1] = card
			return True
		else:
			return False
		
	def move_card_from_row_to_deck(self, row:int, deck:int):
		if self.decks[deck-1] + 1 == self.rows[row-1][-1]:
			card = self.rows[row-1].pop()
			self.decks[deck-1] = card
			return True
		else:
			return False

class HumanController(Controller):
	def __init__(self):
		super().__init__()

	def play(self, card):
		print("Type 'help' to see the controls")
		print(f"\nA(n) {card} has been pulled. Where would you like to place it?")
		self.display_game()
		self.moves(card)
		
	def moves(self, card):
		played_card = False
		while True:
			cmd = input().split()
			try:
				match(cmd[0]):
					case "help":
						print("""
Below are the acceptable commands. You can give any number of legal commands in 1 turn, remember to only use the
'done' command when you are FULLY done with your turn.
'pr _':		This command places the pulled card on the specified row. Example: 'pr 2' places the number on the second row.
'pd _':		This command places the pulled card on the specified deck. This will gracefully fail if the pulled number is
			not exactly 1 higher than the value currently placed on that deck. Example: 'pd 2' places the number on the second deck,
			if possible.
'mc _ _':	This command moves the top card from a specified row to a specified deck. This will gracefully fail if the moved number is
			not exactly 1 higher than the value currently placed on that deck. Example: 'mc 3 1' moves the top card from the third row,
			to the first deck, if possible.
'done':		This command ends your turn.
							""")
					case "pr":
						if not played_card:
							self.place_card_on_row(card, int(cmd[1]))
							print(f"{card} has been placed on row {cmd[1]}")
							played_card = True
						else:
							print(f"You have already placed the pulled card!")
						self.display_game()
					case "pd":
						if not played_card:
							if self.place_card_on_deck(card, int(cmd[1])):
								print(f"{card} has been placed on row {cmd[1]}")
								played_card = True
							else:
								print(f"{card} cannot be placed on deck {cmd[1]}, {self.decks[int(cmd[1])]} + 1 =/= {card}")
						else:
							print(f"You have already placed the pulled card!")
						self.display_game()
					case "mc":
						if self.move_card_from_row_to_deck(int(cmd[1]), int(cmd[2])):
							print(f"A card was moved from row {cmd[1]} to deck {cmd[2]}")
						else:
							print(f"You cannot move the card from row {cmd[1]} to deck {cmd[2]}")
						self.display_game()
					case "done":
						if played_card:
							print(f"Turn Finished!")
							return
						else:
							print(f"You must place the pulled card before finishing your turn")
					case _:
						print("Your command was not understood")
						self.display_game()
			except:
				print("Bad input!")

	def display_game(self):
		self.display_rows()
		self.display_decks()

	def display_rows(self):
		for r in self.rows:
			print(r)

	def display_decks(self):
		for d in self.decks:
			print(f"<{d}>")

class AIController(Controller):
	def __init__(self):
		super().__init__()	