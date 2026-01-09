from Board import Board

class Controller():
	def __init__(self):
		pass

	def init(self, board: Board):
		self.board = board

	def play(self, card):
		self.board.set_card(card)
		self.board.display_game()

	def won_game(self):
		return self.board.won_game()

class HumanController(Controller):
	def __init__(self):
		super().__init__()

	def play(self, card):
		super().play(card)
		print("Type 'help' to see the controls")
		print(f"\nA(n) {card} has been pulled. Where would you like to place it?")

		self.moves(card)
		
	def moves(self, card):
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
						if self.board.place_card_on_row(card, int(cmd[1])):
							print(f"{card} has been placed on row {cmd[1]}")
						else:
							print(f"You have already placed the pulled card!")
						self.board.display_game()
					case "pd":
						if self.board.place_card_on_deck(card, int(cmd[1])):
							print(f"{card} has been placed on row {cmd[1]}")
						else:
							print(f"{card} cannot be placed on deck {cmd[1]}, or card was already placed.")
						self.board.display_game()
					case "mc":
						if self.board.move_card_from_row_to_deck(int(cmd[1]), int(cmd[2])):
							print(f"A card was moved from row {cmd[1]} to deck {cmd[2]}")
						else:
							print(f"You cannot move the card from row {cmd[1]} to deck {cmd[2]}")
						self.board.display_game()
					case "done":
						if self.board.get_card_played():
							print(f"Turn Finished!")
							return
						else:
							print(f"You must place the pulled card before finishing your turn")
					case _:
						print("Your command was not understood")
						self.board.display_game()
			except:
				print("Bad input!")

class AIController(Controller):
	def __init__(self):
		super().__init__()	