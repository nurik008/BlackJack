import random
from BlackJack.Card import Card

class Deck():
    def __init__(self):
        self.cards = []
        self.ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self._create_deck()
    
    def _create_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))
        
        random.shuffle(self.cards)
    
    def deal_card(self):
        if len(self.cards) > 0:
            return (self.cards.pop())
        else:
            return ()
     
    