def merge_sort(cards):
    if len(cards) > 1:
        mid = len(cards) // 2
        left_half = cards[:mid]
        right_half = cards[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].compare(right_half[j]) <= 0:
                cards[k] = left_half[i]
                i += 1
            else:
                cards[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            cards[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            cards[k] = right_half[j]
            j += 1
            k += 1

import random

class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def compare(self, card):
        return (self.rank, self.suit) < (card.rank, card.suit)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num):
        return [self.cards.pop() for _ in range(num)]

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class Player:
    def __init__(self):
        self.hand = []
        self.rounds_won = 0

    def sort_hand(self):
        merge_sort(self.hand)

    def play_card(self, index):
        if 0 <= index < len(self.hand):
            return self.hand.pop(index)
        raise IndexError("Invalid card index")

    def __str__(self):
        return f"Player's hand: {', '.join(str(card) for card in self.hand)}"

class Opponent(Player):
    def play_card_auto(self):
        if self.hand:
            return self.hand.pop(0)  # Play the first card automatically
        raise IndexError("No cards to play")

class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.opponent = Opponent()
        self.current_round = 0

    def start_game(self):
        self.player.hand = self.deck.deal(5)
        self.opponent.hand = self.deck.deal(5)
        self.player.sort_hand()
        self.opponent.sort_hand()
        self.play_round()

    def play_round(self):
        self.current_round += 1
        print(f"\nRound {self.current_round}")
        print(self.player)
        print(f"Opponent's hand: {len(self.opponent.hand)} cards")

        while True:
            try:
                index = int(input("Choose a card index to play (0 to {}): ".format(len(self.player.hand) - 1)))
                player_card = self.player.play_card(index)
                print(f"You played: {player_card}")
                break
            except (ValueError, IndexError) as e:
                print(f"Error: {str(e)}. Please enter a valid index.")

        opponent_card = self.opponent.play_card_auto()
        print(f"Opponent played: {opponent_card}")

        # Compare cards to determine the round winner
        if player_card.compare(opponent_card):
            self.player.rounds_won += 1
            print("You win this round!")
        else:
            self.opponent.rounds_won += 1
            print("Opponent wins this round!")

        self.player.sort_hand()
        self.opponent.sort_hand()

        # Ask if the game should continue
        if len(self.player.hand) > 0 and len(self.opponent.hand) > 0:
            self.play_round()
        else:
            print("Game over!")
            print(f"You won {self.player.rounds_won} rounds.")
            print(f"Opponent won {self.opponent.rounds_won} rounds.")

if __name__ == "__main__":
    game = CardGame()
    game.start_game()
