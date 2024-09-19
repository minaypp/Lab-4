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
        self.hand.sort(key=lambda card: (card.rank, card.suit))

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
        print(f"Round {self.current_round}")
        print(self.player)
        print(f"Opponent's hand: {len(self.opponent.hand)} cards")
        
        # Simulate player's turn
        try:
            index = int(input("Choose a card index to play (0 to {}): ".format(len(self.player.hand) - 1)))
            player_card = self.player.play_card(index)
            print(f"You played: {player_card}")
        except (ValueError, IndexError) as e:
            print(f"Error: {str(e)}. Please try again.")
            return
        
        # Simulate opponent's turn
        opponent_card = self.opponent.play_card_auto()
        print(f"Opponent played: {opponent_card}")

        # Compare cards and determine round winner (simplified)
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

if __name__ == "__main__":
    game = CardGame()
    game.start_game()
