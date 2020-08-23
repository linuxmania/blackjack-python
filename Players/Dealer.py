from Players.Player import Player

class Dealer(Player):

    def __str__(self):
        return f"Dealer is {self.name}"

    def reportUpCard(self):
        print("Dealer is",  self.name,  "showing:")
        print(self.hand[1])
