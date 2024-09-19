import random

class Card:
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
             'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __lt__(self, other):
        return self.get_rank_value() < other.get_rank_value()

    def get_rank_value(self):
        return self.ranks[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num):
        return [self.cards.pop() for _ in range(num)] if len(self.cards) >= num else []

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.wins = 0

    def receive_cards(self, cards):
        self.hand.extend(cards)
        self.sort_hand()  # Sort the hand using Merge Sort or Quick Sort

    def sort_hand(self):
        # Uncomment the sorting algorithm you want to use:
        self.hand = self.merge_sort(self.hand)  # Using Merge Sort
        # self.quick_sort(self.hand, 0, len(self.hand) - 1)  # Using Quick Sort

    # Merge Sort Implementation
    def merge_sort(self, hand):
        if len(hand) > 1:
            mid = len(hand) // 2
            left_half = hand[:mid]
            right_half = hand[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    hand[k] = left_half[i]
                    i += 1
                else:
                    hand[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                hand[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                hand[k] = right_half[j]
                j += 1
                k += 1

        return hand

    # Quick Sort Implementation
    def quick_sort(self, hand, low, high):
        if low < high:
            pi = self.partition(hand, low, high)
            self.quick_sort(hand, low, pi - 1)
            self.quick_sort(hand, pi + 1, high)

    def partition(self, hand, low, high):
        pivot = hand[high]
        i = low - 1
        for j in range(low, high):
            if hand[j] < pivot:
                i += 1
                hand[i], hand[j] = hand[j], hand[i]
        hand[i+1], hand[high] = hand[high], hand[i+1]
        return i + 1

    def play_card(self, index):
        if 0 <= index < len(self.hand):
            return self.hand.pop(index)
        return None

    def show_hand(self):
        return ', '.join(f"{i+1}. {card}" for i, card in enumerate(self.hand))

    def increment_wins(self):
        self.wins += 1

class Opponent(Player):
    def simulate_turn(self):
        # Simple AI: randomly select a card to play
        return self.play_card(random.randint(0, len(self.hand) - 1))

class CardGame:
    def __init__(self, num_cards=5):
        self.deck = Deck()
        self.player = Player('Player 1')
        self.opponent = Opponent('Computer')
        self.num_cards = num_cards

    def deal_cards(self):
        self.deck.shuffle()
        self.player.receive_cards(self.deck.deal(self.num_cards))
        self.opponent.receive_cards(self.deck.deal(self.num_cards))

    def compare_cards(self, card1, card2):
        if card1 and card2:
            return card1 > card2
        return False

    def player_turn(self):
        print(f"\n{self.player.name}'s turn!")
        print(f"Your hand: {self.player.show_hand()}")

        valid_input = False
        while not valid_input:
            try:
                choice = int(input("Select a card to play by number: ")) - 1
                if 0 <= choice < len(self.player.hand):
                    valid_input = True
                    return self.player.play_card(choice)
                else:
                    print(f"Invalid choice. Select a number between 1 and {len(self.player.hand)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def opponent_turn(self):
        print(f"\n{self.opponent.name}'s turn!")
        return self.opponent.simulate_turn()

    def play_game(self):
        self.deal_cards()
        print(f"Dealing {self.num_cards} cards to each player...\n")

        while self.player.hand and self.opponent.hand:
            # Player's turn
            player_card = self.player_turn()
            print(f"You played: {player_card}")

            # Opponent's turn
            opponent_card = self.opponent_turn()
            print(f"Opponent played: {opponent_card}")

            # Compare cards
            if self.compare_cards(player_card, opponent_card):
                print(f"{self.player.name} wins this round!")
                self.player.increment_wins()
            else:
                print(f"{self.opponent.name} wins this round!")
                self.opponent.increment_wins()

        # Display final results
        print(f"\nFinal score: {self.player.name} - {self.player.wins}, {self.opponent.name} - {self.opponent.wins}")
        if self.player.wins > self.opponent.wins:
            print(f"{self.player.name} wins the game!")
        else:
            print(f"{self.opponent.name} wins the game!")

if __name__ == "__main__":
    game = CardGame(num_cards=5)
    game.play_game()
