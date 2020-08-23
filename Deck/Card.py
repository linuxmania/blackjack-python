class Card:

    def __init__(self,name,suit,value):
        self.name = name
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.name} of {self.suit}"
