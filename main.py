from random import shuffle
from classes.Card import Card
from classes.Deck import Deck
from classes.Foundation import Foundation


def new_game():
    cards = []
    # generates new Deck
    for i in range(4):      # cards
        for j in range(13): # suits
            cards.append(Card(j, i))
    
    deck = Deck(cards)
    deck.shuffle()
    deck.print()

new_game()
# # Test cards
# ace_of_spades = Card(0, 3)
# two_of_spades = Card(1, 3)

# # Try to insert two spades card into empty spades, should fail
# spades_foundation = Foundation(3)
# spades_foundation.insert_card(two_of_spades)
# print(spades_foundation.get_foundation_values())

# # Try to insert ace then two of spaces, should achieve success
# spades_foundation = Foundation(3)
# spades_foundation.insert_card(ace_of_spades)
# spades_foundation.insert_card(two_of_spades)
# print(spades_foundation.get_foundation_values())

# # Try to insert spades card into hearts, should fail
# hearts_foundation = Foundation(2)
# print('Two of spades into hearts: ', hearts_foundation.insert_card(ace_of_spades))