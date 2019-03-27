from random import shuffle

SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


class Deck:
    def __init__(self):
        print("creating a new deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]
        """
        este for de cima é igual a esse de baixo
        allcards = []
        for r in RANKS:
            for s in SUITE:
                mycards.append((s,r))
        """

    def shuffle(self):
            print("shuffling the deck")
            shuffle(self.allcards)

    def split_in_half(self):
            return (self.allcards[:26],self.allcards[26:])

class Hand:

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)
        #o extend funciona assim a = [1,2], b = [3,4] a.extend(b)=[1,2,3,4],
        #o apennd vai ser diferente, a.append(b)=[1,2,[3,4]]
    def remove_card(self):
        return self.cards.pop()#o pop por default ele tira o ultimo elemento da lista, se quiser especificar passa a posição no ()

class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards()) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        #retornar True se o jogador tiver cartas
        return len(self.hand.cards) != 0

print("welcome to the war, let's begin")
#create a new deck and divide it in half
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

#create both players
comp = Player("computer",Hand(half1))

name = input("whats is your name? ")
user = Player(name,Hand(half2))

total_rounds = 0
war_counts = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("time for a new round")
    print("here are the curretn standing")
    print(user.name+"has the current"+str(len(user.hand.cards)))
    print(comp.name+"has the current"+str(len(user.hand.cards)))
    print("play a card")
    print("\n")

    table_cards = []
    war_count = 0
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print("war")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
print("game over, number of rounds:"+str(total_rounds))
print("a war happenned: "+str(war_count)+"times")
