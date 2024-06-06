class DiamondsUI:
    def __init__(self, game):
        self.game = game

    def start_game(self):
        print("Welcome to the Diamonds Game!")
        self.game.deal_cards()
        while not self.game.is_game_over():
            self.play_round()
        self.display_winner()

    def play_round(self):
        current_diamond = self.game.diamond_deck[self.game.current_round]
        print(f"Round {self.game.current_round + 1}")
        print(f"Diamond Card: {current_diamond}")
        for i, player in enumerate(self.game.players):
            print(f"Player {i + 1}'s turn")
            if isinstance(player, AIPlayer):
                bid = player.place_bid(current_diamond)
                if bid:
                    print(f"AI Player {i + 1} bids: {bid}")
                else:
                    print(f"AI Player {i + 1} passes")
            else:
                bid = self.get_player_bid(player)
            player.hand.remove(bid)
        self.game.play_round()
        self.display_scores()

    def get_player_bid(self, player):
        print(f"Your hand: {player.hand}")
        bid = input("Enter your bid: ")
        while bid not in player.hand:
            print("Invalid bid. Try again.")
            bid = input("Enter your bid: ")
        return bid

    def display_scores(self):
        scores = self.game.get_scores()
        for i, score in enumerate(scores):
            print(f"Player {i + 1} Score: {score}")

    def display_winner(self):
        scores = self.game.get_scores()
        max_score = max(scores)
        winners = [i for i, score in enumerate(scores) if score == max_score]
        print("Game Over!")
        if len(winners) > 1:
            print(f"It's a tie between players: {', '.join([str(w + 1) for w in winners])}")
        else:
            print(f"Player {winners[0] + 1} wins with {max_score} points!")

# Running the game
if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    game = DiamondsGame(num_players)
    ui = DiamondsUI(game)
    ui.start_game()
