from BlackJack.Deck import Deck

class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.score = 0
        self.standing = False

    def add_card(self, card):
        self.cards.append(card)
        self.score += card.value
        
    def ntexs(self):
        Ace_enough = False
        if self.score > 21:
            for card in self.cards:
                if card.rank == "A" and card.value == 11:
                    card.value = 1
                    self.score -= 10
                    if self.score <= 21:
                        Ace_enough = True
            if Ace_enough == False:
                return False
        return True

    def stand(self):
        self.standing = True