import random
from Deck.Card import Card

class Deck:
    deck = []
    shuffled_deck = []
    tmp_deck = []

    def getShuffledDeck(self):
        for card in self.deck:
            self.tmp_deck.append(card)
        size = len(self.deck)
        while (size > 0):
            self.shuffled_deck.append(self.tmp_deck.pop(random.randint(0, size - 1)))
            size -= 1
        return self.shuffled_deck

    deck.append(Card("Ace", "Spades", 11))
    deck.append(Card("Ace", "Hearts", 11))
    deck.append(Card("Ace", "Diamonds", 11))
    deck.append(Card("Ace", "Clubs", 11))
    deck.append(Card("Two", "Spades", 2))
    deck.append(Card("Two", "Hearts", 2))
    deck.append(Card("Two", "Diamonds", 2))
    deck.append(Card("Two", "Clubs", 2))
    deck.append(Card("Three", "Spades", 3))
    deck.append(Card("Three", "Hearts", 3))
    deck.append(Card("Three", "Diamonds", 3))
    deck.append(Card("Three", "Clubs", 3))
    deck.append(Card("Four", "Spades", 4))
    deck.append(Card("Four", "Hearts", 4))
    deck.append(Card("Four", "Diamonds", 4))
    deck.append(Card("Four", "Clubs", 4))
    deck.append(Card("Five", "Spades", 5))
    deck.append(Card("Five", "Hearts", 5))
    deck.append(Card("Five", "Diamonds", 5))
    deck.append(Card("Five", "Clubs", 5))
    deck.append(Card("Six", "Spades", 6))
    deck.append(Card("Six", "Hearts", 6))
    deck.append(Card("Six", "Diamonds", 6))
    deck.append(Card("Six", "Clubs", 6))
    deck.append(Card("Seven", "Spades", 7))
    deck.append(Card("Seven", "Hearts", 7))
    deck.append(Card("Seven", "Diamonds", 7))
    deck.append(Card("Seven", "Clubs", 7))
    deck.append(Card("Eight", "Spades", 8))
    deck.append(Card("Eight", "Hearts", 8))
    deck.append(Card("Eight", "Diamonds", 8))
    deck.append(Card("Eight", "Clubs", 8))
    deck.append(Card("Nine", "Spades", 9))
    deck.append(Card("Nine", "Hearts", 9))
    deck.append(Card("Nine", "Diamonds", 9))
    deck.append(Card("Nine", "Clubs", 9))
    deck.append(Card("Ten", "Spades", 10))
    deck.append(Card("Ten", "Hearts", 10))
    deck.append(Card("Ten", "Diamonds", 10))
    deck.append(Card("Ten", "Clubs", 10))
    deck.append(Card("Jack", "Spades", 10))
    deck.append(Card("Jack", "Hearts", 10))
    deck.append(Card("Jack", "Diamonds", 10))
    deck.append(Card("Jack", "Clubs", 10))
    deck.append(Card("Queen", "Spades", 10))
    deck.append(Card("Queen", "Hearts", 10))
    deck.append(Card("Queen", "Diamonds", 10))
    deck.append(Card("Queen", "Clubs", 10))
    deck.append(Card("King", "Spades", 10))
    deck.append(Card("King", "Hearts", 10))
    deck.append(Card("King", "Diamonds", 10))
    deck.append(Card("King", "Clubs", 10))
