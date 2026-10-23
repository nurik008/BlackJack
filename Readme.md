# BlackJack

A terminal-based blackjack game written in Python. Play against a dealer, place bets using a virtual balance, and choose when to hit or stand.

This is a learning project built around classes for cards, a deck, and players. It uses only the Python standard library.

## Features

- A shuffled deck of 52 cards.
- Player names and readable card descriptions.
- A starting balance of $1,000 in virtual money.
- Whole-number bet validation against the available balance.
- Hit and stand actions.
- A dealer that draws until its score reaches at least 17.
- Win, loss, and tie outcomes with balance updates.
- Replay with a fresh deck while keeping the remaining balance.

## Requirements

- Python 3.6 or newer, available from your terminal.
- No third-party packages are required.

## Run the game

Download or clone this repository, open a terminal in the project folder, and run:

```bash
python main.py
```

Depending on your installation, use `python3 main.py` on macOS or Linux, or `py main.py` on Windows.

## How to play

1. Enter your name. You and the dealer each receive two cards; only one dealer card is initially shown.
2. Enter a whole-number bet between 1 and your current balance.
3. Enter `h` to **hit** and draw another card, or `s` to **stand** and finish your turn.
4. If you exceed 21, you lose the round. Otherwise, the dealer takes its turn and the scores are compared.
5. Enter `y` to play another round or `n` to leave. Play also ends when your balance reaches zero.

The aim is to finish closer to 21 than the dealer without exceeding it.

### Card values

| Card | Value |
| --- | --- |
| 2–10 | Face value |
| Jack, Queen, King | 10 |
| Ace | Starts at 11 and can be reduced to 1 when adjusting an over-21 hand |

### Bets and payouts

Your bet is deducted before your turn begins.

| Result | Amount returned | Net change |
| --- | --- | --- |
| Win | Twice the bet | Gain the bet amount |
| Loss | Nothing | Lose the bet amount |
| Tie | Original bet | No change |

For example, a $100 bet from a $1,000 balance leaves you with $1,100 after a win, $900 after a loss, or $1,000 after a tie.

Wins involving blackjack use the same payout as other wins; there is no separate 3:2 payout.

## Example interaction

An illustrative start to a round (cards vary because the deck is shuffled):

```text
Enter your name: Alex
Alex's hand: ['10 of Hearts', '8 of Clubs'] (Score: 18)
Dealer's hand: ['7 of Diamonds']
You have $1000.
How much would you like to bet? 100
You have bet $100.
Would you like to hit or stand? (h/s) s
```

## Project structure

```text
BlackJack/
├── main.py              # Input, betting, turns, results, and replay
├── Readme.md
└── BlackJack/
    ├── __init__.py
    ├── Card.py          # Card rank, suit, value, and display
    ├── Deck.py          # Deck creation, shuffling, and dealing
    └── Player.py        # Player hand, score adjustment, and standing
```
