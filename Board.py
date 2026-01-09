class Board():
	def __init__(self, row_count, deck_count, max_card):
		self.row_count = row_count
		self.deck_count = deck_count
		self.max_card = max_card

		self.card = 0
		self.card_played = True

		self.rows = [[] for _ in range(row_count)]
		self.decks = [0 for _ in range(deck_count)]

	def won_game(self):
		for d in self.decks:
			if d != self.max_card:
				return False
		return True

	def place_card_on_row(self, card:int, row:int):
		if self.card_played == False:
			self.card_played = True
			self.card = 0
			self.rows[row-1].append(card)
			return True
		return False
	
	def place_card_on_deck(self, card:int, deck:int):
		if self.card_played == False:
			if self.decks[deck-1] + 1 == card:
				self.card_played = True
				self.card = 0
				self.decks[deck-1] = card
				return True
		return False
		
	def move_card_from_row_to_deck(self, row:int, deck:int):
		if self.decks[deck-1] + 1 == self.rows[row-1][-1]:
			card = self.rows[row-1].pop()
			self.decks[deck-1] = card
			return True
		else:
			return False

	def set_card(self, card):
		self.card = card
		self.card_played = False

	def get_card_played(self):
		return self.card_played

	def display_game(self):
		self.display_rows()
		self.display_decks()

	def display_rows(self):
		for r in self.rows:
			print(r)

	def display_decks(self):
		for d in self.decks:
			print(f"<{d}>")