import random

### 1. Card Class ###
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    # For sorting purposes: comparison by rank, then by suit
    def __lt__(self, other):
        rank_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suit_order = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        if self.rank == other.rank:
            return suit_order.index(self.suit) < suit_order.index(other.suit)
        return rank_order.index(self.rank) < rank_order.index(other.rank)

### 2. Deck Class ###
class Deck:
    def __init__(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, num_cards):
        hand = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return hand

### 3. Player Class ###
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def receive_cards(self, cards):
        self.hand.extend(cards)
    
    # Use an efficient sorting algorithm (Merge Sort)
    def sort_hand(self):
        self.hand = merge_sort(self.hand)
    
    def play_card(self):
        if self.hand:
            return self.hand.pop(0)  # Plays the first (smallest) card in the hand
        else:
            return None
    
    def show_hand(self):
        return ', '.join([str(card) for card in self.hand])

### 4. Opponent Class (AI) ###
class Opponent(Player):
    def simulate_turn(self):
        if self.hand:
            print(f"{self.name} played: {self.play_card()}")
        else:
            print(f"{self.name} has no more cards to play!")

### 5. Merge Sort (for sorting the hand) ###
def merge_sort(cards):
    if len(cards) <= 1:
        return cards
    mid = len(cards) // 2
    left = merge_sort(cards[:mid])
    right = merge_sort(cards[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

### 6. Game Logic ###
class CardGame:
    def __init__(self, num_cards_per_hand):
        self.deck = Deck()
        self.deck.shuffle()
        self.num_cards_per_hand = num_cards_per_hand
        self.player = Player("Player")
        self.opponent = Opponent("Opponent")
    
    def deal_cards(self):
        player_hand = self.deck.deal(self.num_cards_per_hand)
        opponent_hand = self.deck.deal(self.num_cards_per_hand)
        
        self.player.receive_cards(player_hand)
        self.opponent.receive_cards(opponent_hand)
        
        print("Cards dealt.")
        print(f"Your hand: {self.player.show_hand()}")
        print(f"{self.opponent.name}'s hand: [Hidden]")
    
    def sort_hands(self):
        print("\nSorting hands...\n")
        self.player.sort_hand()
        self.opponent.sort_hand()
        
        print(f"Your sorted hand: {self.player.show_hand()}")
    
    def play_game(self):
        self.deal_cards()
        self.sort_hands()
        
        round_number = 1
        while self.player.hand or self.opponent.hand:
            print(f"\n--- Round {round_number} ---")
            player_card = self.player.play_card()
            if player_card:
                print(f"You played: {player_card}")
            else:
                print("You have no more cards to play!")
            
            self.opponent.simulate_turn()
            round_number += 1

        print("\nGame Over!")
        if len(self.player.hand) > len(self.opponent.hand):
            print("You win!")
        elif len(self.opponent.hand) > len yours:
            print("Opponent wins!")
        else:
            print("It's a tie!")
        

### 7. Running the Game ###
if __name__ == "__main__":
    # Start the game with 5 cards per hand
    game = CardGame(num_cards_per_hand=5)
    game.play_game()

