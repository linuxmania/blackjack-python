from Deck.Deck import Deck
from Players.Player import Player
from Players.Dealer import Dealer

deck = Deck()
shuffled_deck = deck.getShuffledDeck()

players = []
player1hand=[]
player2hand=[]
dealerhand=[]
players.append(Player("Diamonds",player1hand, False))
players.append(Player("Rust",player2hand, False))
dealer = Dealer("Lefty",dealerhand, False)

for player in players:
    player.addCard(shuffled_deck.pop(0))
dealer.addCard(shuffled_deck.pop(0))

for player in players:
    player.addCard(shuffled_deck.pop(0))
dealer.addCard(shuffled_deck.pop(0))

for player in players:
    print(player)
    player.reportHand()

dealer.reportUpCard()

print('\n' * 1)

for player in players:
    player.processHand(shuffled_deck)

dealer.processHand(shuffled_deck)

for player in players:
    player.reportResults(dealer.getValue(),dealer.busted)
