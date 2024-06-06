class Strategy:
    def optimal_bid(self, current_bid, hand):
        # Find the lowest card that beats the current bid
        sorted_hand = sorted(hand)
        for card in sorted_hand:
            if self.card_value(card) > self.card_value(current_bid):
                return card
        return None  # No valid bid possible
    
    def card_value(self, card):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return values[card]

    def adjust_bid_share(self, diamond_points, num_players):
        # Calculate the share of points if multiple players bid the same
        return diamond_points / num_players

# Example integration with the Player class
class AIPlayer(Player):
    def __init__(self):
        super().__init__()
        self.strategy = Strategy()

    def place_bid(self, current_diamond):
        # Determine the optimal bid using the strategy
        return self.strategy.optimal_bid(current_diamond, self.hand)
