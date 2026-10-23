class Card():
    def __init__(self, suit, rank):
        self._possible_ranks = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
        self.suit = suit
        self.rank = rank
        self.value = self._possible_ranks[rank]
    
    def __str__(self):
        return f"({self.rank} of {self.suit})"