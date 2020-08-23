class Player:

    def __init__(self,name,hand,busted):
        self.name = name
        self.hand = hand
        self.busted = busted

    def __str__(self):
        return f"Player is {self.name}"

    def addCard(self, card):
        self.hand.append(card)

    def reportBusted(self):
        self.reportHand()
        print("Busted!")
        print()

    def reportHand(self):
        for card in self.hand:
            print(card)
        print("Hand Value: ", self.getValue())
        print()

    def reportResults(self,dealerValue,dealerBusted):
        print(self.name)
        if(self.busted):
            print("Busted!!")
        elif(dealerBusted):
            print("Winner!! (Dealer Busted)")
        elif(self.getValue() > dealerValue):
            print("Winner!!")
        elif(self.getValue() < dealerValue):
            print("Loser :(")
        else:
            print("Push :-|")
        print()

    def getValue(self):
        self.value = 0
        for card in self.hand:
            self.value += card.value
        return self.value

    def devalueAce(self):
        for card in self.hand:
            if(card.name == "Ace"):
                if (card.value == 11):
                    card.value = 1
                    break

    def processHand(self,deck):
        while 1:
            print(self)
            self.reportHand()
            print("Hit (y=yes)?")

            a = input()

            if (a == 'y'):
                self.addCard(deck.pop(0))
            else: break

            if(self.getValue() > 21):
                self.devalueAce()

            if(self.getValue() > 21):
                self.busted = True
                self.reportBusted()
                break
