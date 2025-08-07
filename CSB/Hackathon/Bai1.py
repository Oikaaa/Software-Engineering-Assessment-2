import random
deck = []

for suit in ["spade", "club", "diamond", "heart"]:
    for rank in range(2,15):
        deck.append({"suit": suit, "rank": rank})

def special_card(card):
    if card["rank"] == 14:
        return "Ace"
    elif card["rank"] == 11:
        return "Jack"
    elif card["rank"] == 12:
        return "Queen"
    elif card["rank"] == 13:
        return "King"
    else:
        return card["rank"]

class Card:
    def __init__(self, deck):
        self.value = deck[0]["rank"]
        self.suit = deck[0]["suit"]

    def __str__(self):
        return str(self.value) + " of " + self.suit

class Deck:
    def __init__(self, deck):
        self.deck = deck

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def deal_a_card(self):
        card = self.deck.pop(0)
        return str(special_card(card)) + " of " + card["suit"]

    def sort(self):
        suit_order = {"spade": 0, "club": 1, "diamond": 2, "heart": 3}
        self.deck = sorted(self.deck, key=lambda card: (suit_order[card["suit"]], card["rank"]))
        return self.deck 

    def __str__(self):
        string = ""
        for card in self.deck:
            string += str(special_card(card)) + " of " + card["suit"] + ", "
        return string

FirstCard = Card(deck)

deckClass = Deck(deck)

deckClass.shuffle()

print(deckClass)
print("(---------------------)")

deckClass.sort()

print(deckClass)

print("(---------------------)")

Take_away_card = deckClass.deal_a_card()

print(Take_away_card)
print(deckClass)