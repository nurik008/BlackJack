from BlackJack.Player import Player
from BlackJack.Deck import Deck

playing = True
cash = 1000
deck = Deck()
while cash and playing:
    # Get player name and create player and dealer objects
    player = Player(input("Enter your name: "))
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    
    dealer = Player("Dealer")
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    
    print(f"{player.name}'s hand: {[card.rank + ' of ' + card.suit for card in player.cards]} (Score: {player.score})")
    print(f"{dealer.name}'s hand: {[dealer.cards[0].rank + ' of ' + dealer.cards[0].suit]}")
    
    # Betting phase
    print(f"You have ${cash}.")
    while True:
        try:
            bet = int(input("How much would you like to bet? "))
            if 0 < bet <= cash:
                break
            print(f"Enter an amount between 1 and {cash}.")
        except ValueError:
            print("Please enter a whole number.")
    cash -= bet
    print(f"You have bet ${bet}.")
    
    # Gameplay phase
    # Player's turn
    while not player.standing and player.ntexs():
        if not player.standing:
            action = input("Would you like to hit or stand? (h/s) ")
            while action.lower() not in ["h", "s"]:
                action = input("Invalid input. Please enter 'h' to hit or 's' to stand: ")
            if action.lower() == "h":
                player.add_card(deck.deal_card())
                if not player.ntexs():
                    break
                else:
                    print(f"{player.name}'s hand: {[card.rank + ' of ' + card.suit for card in player.cards]} (Score: {player.score})")
            elif action.lower() == "s":
                player.stand()
                print(f"{player.name}'s hand: {[card.rank + ' of ' + card.suit for card in player.cards]} (Score: {player.score})")
                break

    if not player.ntexs():
        print(f"{player.name} has busted with a score of {player.score}. Dealer wins!")
        again = input("Do you want to play again? (y/n) ").lower()
        if again == "n":
            playing = False
            print(f"You leave the game with ${cash}.")
            continue
        elif again == "y":
            deck = Deck()
            continue
        
    # Dealer's turn 
    else:
        while dealer.score < 17:
            dealer.add_card(deck.deal_card())
            if not dealer.ntexs():
                break
    
    # Finalizing results    
    # If someone exceeds 21, the other player wins    
    if not dealer.ntexs():
        print(f"{dealer.name} has busted with a score of {dealer.score}. {player.name} wins!")
        cash += bet * 2
    
    # Determine winner
    elif player.standing:
        if dealer.score > player.score:
            print(f"{dealer.name} wins with a score of {dealer.score}.")
        elif dealer.score < player.score:
            print(f"{player.name} wins with a score of {player.score}.")
            cash += bet * 2
        elif dealer.score == player.score and dealer.score == 21:
            if len(player.cards) == 2 and len(dealer.cards) > 2:
                print(f"{player.name} wins with a blackjack!")
                cash += bet * 2
            elif len(dealer.cards) == 2 and len(player.cards) > 2:
                print(f"{dealer.name} wins with a blackjack!")
            elif len(player.cards) == 2 and len(dealer.cards) == 2:
                print("It's a tie!")
                cash += bet
        else:    
            print("It's a tie!")
            cash += bet
    
    again = input("Do you want to play again? (y/n) ").strip().lower()
    if again == "n":
        playing = False
        print(f"You leave the game with ${cash}.")
        break
    elif again == "y":
        deck = Deck()
        continue